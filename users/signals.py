from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save,sender=User)
def create_profile(sender, instance, created,**kwargs):

    if created == True:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email = user.email,
            name = user.first_name,
        )
        print(user.username)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance,**kwargs):
    user = instance.user
    user.delete()