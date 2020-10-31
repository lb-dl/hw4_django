from user.models import User

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created: # noqa
        print('Created') # noqa
    else:   # noqa
        print('Exists') # noqa


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, *args, **kwargs):
    instance.last_name = instance.last_name.title()
    instance.first_name = instance.first_name.title()
