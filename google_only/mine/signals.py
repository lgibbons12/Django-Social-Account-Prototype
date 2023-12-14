# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from allauth.socialaccount.models import SocialAccount

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        social_account = SocialAccount.objects.filter(user=instance).first()
        if social_account:
            # Social account exists, retrieve the associated user
            user_profile = UserProfile.objects.filter(user=social_account.user).first()
            if not user_profile:
                UserProfile.objects.create(user=social_account.user)
        else:
            # Social account doesn't exist, create a new user profile
            UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
