from django.contrib import admin

# Register your models here.
from .models import Contact, AskQuestion, CommonQuestion, Review
admin.site.register(Contact)
admin.site.register(CommonQuestion)
admin.site.register(AskQuestion)
admin.site.register(Review)
