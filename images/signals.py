from django.db.models.signals import m2m_changed
from django.dispatch.dispatcher import receiver

from images.models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def users_liked_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
