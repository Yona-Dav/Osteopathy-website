from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.views import LoginView
from .models import Profile, MedicalProfile
from django.contrib.auth.models import User
from .forms import SignupForm, MyAuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage, send_mail
from visitors.tokens import account_activation_token
from django.http import HttpResponse
from .forms import ProfileForm, MedicalProfileForm


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
        self.object.is_active = True
        self.object = form.save()
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
        login(request, user)
        return redirect('my_profile')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class ProfileUpdateView(UpdateView, LoginRequiredMixin ):
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


