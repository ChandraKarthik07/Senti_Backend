from django.test import TestCase
import pandas as pd
import numpy as np
# Create your tests here.
import requests
from datetime import datetime
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



def process_data(rawData):

    processed_data = []
    for entry in rawData:
        date = entry["date"].split(", ")[0]
        subs_gain = int(entry["channel_subs"].split(", ")[0].replace("+", "").replace("--", "0").replace("LIVE", "0").replace("K", "000"))
        subs = np.int64(entry["channel_subs"].split(", ")[-1].replace("K", "000").replace("--", "0").replace("LIVE", "0"))
        views_gain = np.int64(entry["overall_views"].split(", ")[0].replace("+", "").replace("--", "0").replace("LIVE", "0").replace(",", ""))
        views = np.int64(entry["overall_views"].split(", ")[-1].replace(",", "").replace("--", "0").replace("LIVE", "0"))

        processed_data.append({
            "date": date,
            "day": datetime.strptime(date, "%Y-%m-%d").strftime("%a"),
            "subs_gain": subs_gain,
            "channel_subs": subs,
            "views_gain": views_gain,
            "overall_views": views})

    return processed_data

def transform_json(json_data):
    result = []
    for item in json_data:
        entry = {
            "Category": item["category"],
            "Channel ID": item["snippet"]["channelId"],
            "Video ID": item["snippet"]["resourceId"]["videoId"],
            "Date": item["snippet"]["publishedAt"],
            "Title": item["snippet"]["title"],
            "View Count": item["statistics"]["viewCount"],
            "Like Count": item["statistics"]["likeCount"],
            "Comment Count": item["statistics"]["commentCount"]
        }
        result.append(entry)
    return result

def fetch_google_user_data(access_token):
    url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
