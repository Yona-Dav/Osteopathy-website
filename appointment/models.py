from django.db import models
from accounts.models import User


# Create your models here.

class Schedule(models.Model):
    owner = models.ForeignKey(User, to_field='username', default='yona', on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'date:{self.date} , hour:{self.hour}'

    class Meta:
        ordering = ['date','hour']