from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('userprofile created for first time when the user is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('Userprofile updated')
        except:
            print('if user profile is not avaiable for the user the this condtion')
            UserProfile.objects.create(user=instance)
            print('Userprofile')
