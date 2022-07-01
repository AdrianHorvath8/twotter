import django
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail


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
        
        subject = "Thanks for registration to Twotter"
        message = "We are glad that you sign in to best twitter imitation "

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance,**kwargs):
    user = instance.user
    user.delete()


