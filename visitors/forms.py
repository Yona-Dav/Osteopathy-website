from .models import Contact, CommonQuestion, AskQuestion, Review
from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Review
        exclude = ['timestamp', 'visible']


class CommonQuestionForm(forms.ModelForm):
    class Meta:
        model = CommonQuestion
        exclude = ['date_of_creation']


class AskQuestionForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = AskQuestion
        exclude = ['date_of_creation']

