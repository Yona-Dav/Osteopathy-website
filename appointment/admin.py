from django.contrib import admin

# Register your models here.

from .models import Schedule, Report

admin.site.register(Schedule)
admin.site.register(Report)

