from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile, User


@receiver(post_save, sender=User)
def my_callback(sender, instance, created, **kwargs):
    if created:
        prof = Profile.objects.create(user=instance)