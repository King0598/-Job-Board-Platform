from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Application
from .services import send_application_notification

@receiver(post_save, sender=Application)
def application_created(sender, instance, created, **kwargs):
    if created:
        send_application_notification(instance)