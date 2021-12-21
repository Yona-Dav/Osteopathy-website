from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView,PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView
from .models import Profile, MedicalProfile
from django.contrib.auth.models import User
from .forms import SignupForm, MyAuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage, send_mail
from visitors.tokens import account_activation_token
from django.http import HttpResponse
from .forms import ProfileForm, MedicalProfileForm
from staff.models import Exercise
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

class Signup(CreateView):
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('about')
    template_name = 'signup.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object = form.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': self.object,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.object.pk)),
            'token': account_activation_token.make_token(self.object),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        user = authenticate(self.request, username=self.object.username, password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
        return HttpResponse('Please confirm your email address to complete the registration')


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = MyAuthenticationForm


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if user.is_authenticated:
            return redirect('my_profile')
        else:
            return HttpResponse('User not authenticated')
    else:
        return HttpResponse('Activation link is invalid!')


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    fields = ['birth_date','sex','marital_status','phone','address','city','country']
    success_url = reverse_lazy('my_profile')
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile


class MedicalProfileCreateView(LoginRequiredMixin, CreateView):
    model = MedicalProfile
    form_class = MedicalProfileForm
    success_url = reverse_lazy('about')
    template_name = 'medical_profile.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object=form.save()
        return HttpResponseRedirect(self.get_success_url())


class MedicalProfileDetailView(LoginRequiredMixin,DetailView):
    model = MedicalProfile
    template_name = 'medical.html'


class MedicalProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'medical_profile.html'
    model = MedicalProfile
    form_class = MedicalProfileForm
    success_url = reverse_lazy('my_profile')

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProfileViewList(ListView, UserPassesTestMixin):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'

    def test_func(self):
        return self.request.user.is_staff


class ProfileDetailView(DetailView, UserPassesTestMixin):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

    def test_func(self):
        return self.request.user.is_staff

@login_required
def see_my_exercises(request, user_id):
    my_exercises = Exercise.objects.filter(user=user_id)
    return render(request, 'my_exercises.html', {'my_exercises':my_exercises, 'userid': user_id , 'exercises':Exercise.objects.exclude(user=user_id)})


@ staff_member_required
def remove_exercise_from_user(request, exercise_id, user_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    user = get_object_or_404(User, id=user_id)
    user.exercise_set.remove(exercise)
    return redirect('my_exercises', user_id)


@ staff_member_required
def add_exercise_to_user(request,user_id,exercise_id,):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    user = get_object_or_404(User, id=user_id)
    user.exercise_set.add(exercise)
    return redirect('my_exercises', user_id)


@ staff_member_required
def deactivate_profile(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, 'Profile successfully disabled.')
    return redirect('profiles')


class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    template_name = 'password_change.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())


class DonePasswordView(PasswordChangeDoneView, LoginRequiredMixin):
    template_name = 'password_change_done.html'


class ResetPassword(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'


class ResetDonePassword(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class ConfirmResetPassword(PasswordResetConfirmView):
    template_name= 'password_reset_confirm.html'


class CompleteResetPassword(PasswordResetCompleteView):
    template_name= 'password_complete.html'