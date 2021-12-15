from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from .models import Contact, CommonQuestion, AskQuestion, Review
from .forms import ContactForm, CommonQuestionForm, AskQuestionForm, ReviewForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def about(request):
    return render(request, 'about.html')


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        self.object = form.save()
        name = self.object.name

        mail_subject = 'Contact Message'
        message = render_to_string('contact_email.html', {
            'user': self.object,
        })
        from_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, from_email=from_email, to=['ydavid256@gmail.com']
        )
        email.send()

        return render(self.request, 'contact.html', {'name':name})


def osteopathy(request):
    return render(request, 'osteopathy.html')


class CommonQuestionView(ListView):
    model = CommonQuestion
    template_name = 'common_question.html'
    context_object_name = 'questions'


class AskQuestionCreateView(CreateView):
    template_name = 'ask_question.html'
    model = AskQuestion
    form_class = AskQuestionForm

    def form_valid(self, form):
        self.object = form.save()
        name = self.object.name

        mail_subject = 'Question Message'
        message = render_to_string('question_email.html', {
            'user': self.object,
        })
        from_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, from_email=from_email, to=['yona.bohbot@gmail.com']
        )
        email.send()

        return render(self.request, 'ask_question.html', {'name':name})


class ReviewCreateView(CreateView):
    template_name = 'add_review.html'
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        self.object = form.save()
        name = self.object.name

        mail_subject = 'Review Message'
        message = render_to_string('review_email.html', {
            'user': self.object,
        })
        email = EmailMessage(
            mail_subject, message, to=['yona.bohbot@gmail.com']
        )
        email.send()

        return render(self.request, 'add_review.html', {'name': name})


class ReviewView(ListView):
    model = Review
    template_name = 'reviews.html'
    context_object_name = 'reviews'





