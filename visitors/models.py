from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)


class CommonQuestion(models.Model):
    question = models.TextField()
    response = models.TextField()

    def __str__(self):
        return self.question


class AskQuestion(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    RATINGS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.CharField(max_length=100, choices=RATINGS)
    timestamp = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content


