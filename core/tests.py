from django.test import TestCase

# Create your tests here.
import requests

def scrape_channel(channel_name, scan_id):
    # Your code here
    
    # Assuming you have `user_uuid` and `channel_name` defined

  
    
    # Call the external API after completing your function
    api_url = "http://100.100.151.14:8000/scrape_channel/"
    params = {
        "scanID": scan_id,
        "channelUsername": channel_name
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        print("API call successful!")
    else:
        print("API call failed:", response.status_code)
        print(response.text)