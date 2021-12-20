from django.shortcuts import render, redirect
from .models import Schedule, Report
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .forms import ScheduleForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User, Profile
from datetime import datetime
from django.db.models import Q
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string


# Create your views here.


class ScheduleCreateView(CreateView,UserPassesTestMixin):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'add_schedule.html'
    success_url = reverse_lazy('schedules')

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_staff


class ScheduleView(ListView, LoginRequiredMixin):
    model = Schedule
    template_name = 'schedules.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        return super(ScheduleView, self).get_queryset().filter(available=True).filter(owner='yona').filter(Q(date__gt=datetime.today()) | Q(date=datetime.today(), hour__gt=datetime.now().time()))


class ScheduleDeleteView(DeleteView,UserPassesTestMixin):
    model = Schedule
    template_name = 'delete_view.html'
    success_url = reverse_lazy('schedules')
    success_message = "The schedule was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(ScheduleDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff


class ScheduleUpdateView(UserPassesTestMixin,UpdateView):
    model = Schedule
    fields = '__all__'
    success_url = reverse_lazy('schedules')
    template_name = 'add_schedule.html'

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_staff


class ScheduleBookedView(ListView, UserPassesTestMixin):
    model = Schedule
    template_name = 'schedules_booked.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        return super(ScheduleBookedView, self).get_queryset().filter(available=False).exclude(owner='yona').filter(Q(date__gt=datetime.today()) | Q(date=datetime.today(), hour__gt=datetime.now().time()))


@login_required()
def book_appointment(request, schedule_id, booked):
    schedule = Schedule.objects.get(id=schedule_id)
    if booked:
        schedule.available = False
        schedule.save()
        schedule.owner = request.user
        schedule.save()
        name = schedule.owner

        mail_subject = 'Confirm Appointment'
        message = render_to_string('confirmation_email.html', {
            'user': schedule,
        })
        to_email = schedule.owner.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return redirect('my_schedules')


class MyAppointmentsView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = 'my_schedules.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        return super(MyAppointmentsView, self).get_queryset().filter(owner=self.request.user).filter(Q(date__gt=datetime.today()) | Q(date=datetime.today(), hour__gt=datetime.now().time()))


@login_required
def cancel_appointment(request, schedule_id, canceled):
    schedule = Schedule.objects.get(id=schedule_id)
    if canceled:
        schedule.available = True
        schedule.save()
        user = User.objects.filter(username='yona')
        schedule.owner = user.first()
        schedule.save()
        return redirect('my_schedules')


@login_required
def see_date_appointment(request, date_id):
    schedules = Schedule.objects.filter(date=date_id, available=True).filter(Q(date__gt=datetime.today()) | Q(date=datetime.today(), hour__gt=datetime.now().time()))
    return render(request, 'schedule_by_date.html', {'schedules':schedules})


class ReportCreateView(UserPassesTestMixin, CreateView):
    model = Report
    fields = ['content']
    template_name = 'new_report.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        profile_id = self.kwargs['profile_id']
        profile = Profile.objects.get(id=profile_id)
        self.object.profile = profile
        schedule_id = self.kwargs['schedule_id']
        schedule = Schedule.objects.get(id=schedule_id)
        self.object.schedule = schedule
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        profile_id = self.kwargs['profile_id']
        return reverse_lazy('detail_profile', kwargs={'pk': profile_id})


class ReportUpdateView(UserPassesTestMixin,UpdateView):
    model = Report
    fields = ['content']
    template_name = 'new_report.html'

    def get_success_url(self):
        rep_id = self.kwargs['pk']
        rep = Report.objects.get(id=rep_id)
        profile_id = rep.profile.id
        return reverse_lazy('detail_profile', kwargs={'pk': profile_id})

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_staff



