from django.contrib import admin
from .models import Profile, MedicalProfile,FrequencyPain,ActivitiesAggravateCondition, ActivitiesBetterCondition,IntefereWith,Symptoms, FamilyHistory, SufferedMedical, Drink

# Register your models here.
admin.site.register(Profile)
admin.site.register(MedicalProfile)
admin.site.register(FrequencyPain)
admin.site.register(ActivitiesAggravateCondition)
admin.site.register(ActivitiesBetterCondition)
admin.site.register(IntefereWith)
admin.site.register(Symptoms)
admin.site.register(FamilyHistory)
admin.site.register(SufferedMedical)
admin.site.register(Drink)

