from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    SEX = (('Male','Male'),('Female','Female'),('Other','Other'))
    MARITAL = (('Single','Single'),('Married','Married'),('Divorced','Divorced'), ('Widowed','Widowed'),('Separated', 'Separated'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(default='2021-11-11')
    gender = models.CharField(max_length=100, choices=SEX,  blank=True)
    marital_status= models.CharField(max_length=100, choices=MARITAL, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)


class FrequencyPain(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ActivitiesAggravateCondition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ActivitiesBetterCondition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IntefereWith(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Symptoms(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FamilyHistory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SufferedMedical(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MedicalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reason_for_visit = models.CharField(max_length=500)
    symptoms_appear = models.CharField(max_length=200)
    rate_your_pain = models.PositiveSmallIntegerField()
    area_of_pain = models.CharField(max_length=200)
    frequency_of_pain = models.ForeignKey(FrequencyPain, on_delete=models.CASCADE)
    interfere_with = models.ManyToManyField(IntefereWith, blank=True)
    activities_aggravate_condition = models.ManyToManyField(ActivitiesAggravateCondition, blank=True)
    make_pain_better = models.ManyToManyField(ActivitiesBetterCondition, blank=True)
    symptoms = models.ManyToManyField(Symptoms, blank=True)
    suffered_from_medical = models.ManyToManyField(SufferedMedical, blank=True)
    family_history = models.ManyToManyField(FamilyHistory, blank=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    surgical_procedure = models.CharField(max_length=300, blank=True, null=True)
    smoke = models.BooleanField()
    drink = models.ManyToManyField(Drink, blank=True)
    recreational_drugs = models.BooleanField()
