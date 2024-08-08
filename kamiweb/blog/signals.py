from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Reel

@receiver(post_delete, sender=Reel)
def delete_video_file(sender, instance, **kwargs):
    if instance.video:
        instance.video.delete(False)