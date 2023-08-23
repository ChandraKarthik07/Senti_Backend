# from social_django.models import UserSocialAuth
# import requests

# def google_extra_data_pipeline(strategy, details, response, user=None, *args, **kwargs):
#     if user and response.get('access_token'):
#         # Fetch additional data from Google API
#         google_api_data = fetch_google_data(response['access_token'])
        
#         # Update the 'extra_data' dictionary with fetched data
#         user_social_auth = UserSocialAuth.objects.get(user=user, provider='google')
#         user_social_auth.extra_data.update(google_api_data)
#         user_social_auth.save()

# # Function to fetch data from Google API
# def fetch_google_data(access_token):
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
    
#     endpoint_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
    
#     response = requests.get(endpoint_url, headers=headers)
#     data = response.json()
    
#     return data
