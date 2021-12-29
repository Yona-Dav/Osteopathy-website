from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from .models import Profile, MedicalProfile, FrequencyPain, IntefereWith, ActivitiesBetterCondition,ActivitiesAggravateCondition,FamilyHistory,Drink,Symptoms,SufferedMedical


class SignupForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class MyAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
    fields = ['username','password','remember_me']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']


class MedicalProfileForm(forms.ModelForm):
    RATE = [('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]
    reason_for_visit = forms.CharField(
        widget=forms.Textarea,
        label="Reason for visit:")
    symptoms_appear = forms.CharField(
        label='When did symptoms first appear',)
    rate_your_pain = forms.ChoiceField(
        label='Please rate your pain',
        widget=forms.RadioSelect,
        choices=RATE,
    )
    area_of_pain = forms.CharField(
        label="Please precise the area of the body that hurts",)
    frequency_of_pain = forms.ModelChoiceField(
        queryset=FrequencyPain.objects.all(),
        label='How often do you have this pain',
        widget=forms.RadioSelect)
    interfere_with = forms.ModelMultipleChoiceField(
        queryset=IntefereWith.objects.all(),
        label='Does it interfere with:',
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    activities_aggravate_condition = forms.ModelMultipleChoiceField(
        queryset=ActivitiesAggravateCondition.objects.all(),
        label='What activities aggravate your condition? (Check all that apply)',
        widget=forms.CheckboxSelectMultiple,
    )
    make_pain_better = forms.ModelMultipleChoiceField(
        queryset=ActivitiesBetterCondition.objects.all(),
        label='What makes your pain better? (Check all that apply)',
        widget =forms.CheckboxSelectMultiple,
    )
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptoms.objects.all(),
        label='Do you experience the following symptoms? (Check all that apply)',
        widget=forms.CheckboxSelectMultiple
    )
    suffered_from_medical = forms.ModelMultipleChoiceField(
        queryset=SufferedMedical.objects.all(),
        label='Do you or have you ever suffered from the following medical conditions? (Check all that apply)',
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    family_history = forms.ModelMultipleChoiceField(
        queryset=FamilyHistory.objects.all(),
        label='Indicate if you have a family history of any of the following',
        widget=forms.CheckboxSelectMultiple,
        required=False)
    surgical_procedure = forms.CharField(
        label='List all surgical procedures you have had and the times you have been hospitalized',
        required=False,
    )
    drink = forms.ModelMultipleChoiceField(
        queryset=Drink.objects.all(),
        label='Do you drink',
        widget=forms.CheckboxSelectMultiple,
        required=False)


    class Meta:
        model = MedicalProfile
        exclude = ['user']