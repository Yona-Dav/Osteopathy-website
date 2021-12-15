import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osteopath.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import FrequencyPain,ActivitiesAggravateCondition, ActivitiesBetterCondition,IntefereWith,Symptoms, FamilyHistory, SufferedMedical, Drink


def populate_frequency():
    frequency = ['Intermittently','Occasionally','Frequently','Constantly']
    for freq in frequency:
        frequency_pain = FrequencyPain.objects.create(name=freq)


def populate_activities_aggravate():
    activities = ['standing', 'sitting', 'walking', 'bending', 'tension', 'lack of sleep', 'lying down', 'lifting','driving','reaching over head', 'sexual activity','working on the computer','rainy weather']
    for act in activities:
        activities = ActivitiesAggravateCondition.objects.create(name=act)


def populate_better_activities():
    activities = ['Lying down', 'walking', 'sitting','standing', 'medication', 'sleep', 'heat', 'ice', 'massage', 'exercise','streching','traction','corset','biofeedback','compression']
    for act in activities:
        activities_better = ActivitiesBetterCondition.objects.create(name=act)


def populate_interfere():
    interference = ['work','sleep','daily activities', 'recreation']
    for inter in interference:
        interfere = IntefereWith.objects.create(name=inter)


def populate_symptoms():
    symptoms = ['headaches','dizziness','memory loss', 'concentration deficits', 'nausea', 'vomiting', 'weakness','numbness','fatigue','bowel dysfunction','bladder dysfunction', 'irritability','difficulty walking', 'depression','anxiety','weight gain/loss','swelling','hair loss','coldness', 'warmth']
    for symp in symptoms:
        symptom = Symptoms.objects.create(name=symp)


def populate_suffered_medical():
    conditions = ['headaches', 'neck pain', 'upper back pain', 'mid back pain','low back pain', 'shoulder/scapular pain','elbow/upper arm pain', 'hand pain', 'hip/upper leg pain', 'ankle/foot pain', 'jaw pain', 'arthritis', 'rheumatoid arthritis','muscular incoordination', 'high blood presure', 'heart attack','stroke', 'liver desease', 'kidney stones', 'kidney disorders', 'bladder infections','painful urination', 'prostate problems','weight gain/loss','loss of appetite', 'abdominal pain','ulcer','hepatitis','diabetes','excessive thirst', 'frequent urination', 'allergies', 'depression','systemic lupus', 'epilepsy','hiv/aids','visual disturbances', 'cancer', 'tumor', 'dizziness', 'general fatigue']
    for con in conditions:
        suffered = SufferedMedical.objects.create(name=con)


def populate_family_history():
    history =['Rheumatoid arthritis', 'multiple sclerosis', 'diabetes', 'cancer', 'lupus', 'heart disease', 'high blood presure', 'stroke']
    for histo in history:
        family = FamilyHistory.objects.create(name=histo)


def populate_drink():
    drinks = ['alcohol', 'coffee','tea', 'sodas']
    for drink in drinks:
        dr = Drink.objects.create(name=drink)


