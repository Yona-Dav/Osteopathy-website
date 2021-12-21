from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import User, Profile

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_created = models.DateField(auto_now_add=True)
    user = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return self.title


class Instruction(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
