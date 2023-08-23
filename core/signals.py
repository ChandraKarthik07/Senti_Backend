from django.db.models.signals import pre_save
from django.dispatch import receiver
from social_django.models import UserSocialAuth
from .tests import fetch_google_user_data
@receiver(pre_save, sender=UserSocialAuth)
def fetch_google_user_info(sender, instance, **kwargs):
    if instance.pk and instance.provider == 'google-oauth2'and instance.user.google_extra_data is None:
        print("Updating UserSocialAuth instance")
        access_token = instance.extra_data.get('access_token')
        if access_token:
            # Make an API call to Google using the access token
            google_user_info = fetch_google_user_data(access_token)
            print(google_user_info)
            if google_user_info:
                # Update the social authentication record with the retrieved user data
                instance.user.google_extra_data = google_user_info
