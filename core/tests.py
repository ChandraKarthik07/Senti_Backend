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

# def transform_json(json_data):
#     result = []
#     for item in json_data:
#         entry = {
#             "Category": item["category"],
#             "Channel ID": item["snippet"]["channelId"],
#             "Video ID": item["snippet"]["resourceId"]["videoId"],
#             "Date": item["snippet"]["publishedAt"],
#             "Title": item["snippet"]["title"],
#             "View Count": item["statistics"]["viewCount"],
#             "Like Count": item["statistics"]["likeCount"],
#             "Comment Count": item["statistics"]["commentCount"]
#         }
#         result.append(entry)
#     return result

def fetch_google_user_data(access_token):
    url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# def process_videostats(data):
#     df = pd.DataFrame(data)
#     df.rename(columns={
#         "video_stats_id": "index",
#         "vid_id": "Video ID",
#         "date": "Date",
#         "vid_title": "Title",
#         "vid_view_cnt": "View Count",
#         "vid_like_cnt": "Like Count",
#         "vid_comment_cnt": "Comment Count",
#         "category": "Category",
#         "channel": "Channel ID"
#     }, inplace=True)
#     one_two=get_one_two(df)
#     three_four=get_three_four(df)
#     combined_response = {
#         'Latest_20_videos':data,
#         'one_two': one_two,
#         'three_four': three_four
#     }
#     return combined_response


# def get_one_two(df):
#     df['Date'] = pd.to_datetime(df['Date'])
#     df['Week'] = df['Date'].dt.strftime('%Y-%U')
#     df['Month'] = df['Date'].dt.to_period('M')
    
#     videos_per_week = df.groupby('Week')['Category'].count().reset_index()
#     videos_per_month = df.groupby('Month')['Category'].count().reset_index()
#     videos_per_month['Month'] = videos_per_month['Month'].astype(str)
    
#     plot_data = {
#         'videos_per_week': videos_per_week.to_dict(orient='records'),
#         'videos_per_month': videos_per_month.to_dict(orient='records'),
#     }
#     return plot_data

# def get_three_four(data):
#     # Convert numeric columns to numeric types
#     # numeric_columns = ['View Count', 'Like Count', 'Comment Count']
#     # data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
#     # Calculate Engagement Rate
#     data['Engagement Rate'] = (data['Like Count'] + data['Comment Count']) / data['View Count']
    
#     # Sort DataFrame by 'View Count' in descending order
#     sorted_df = data.sort_values(by='View Count', ascending=False)
    
#     # Prepare data for the first bar plot
#     bar_plot_data = sorted_df.head(10)[['View Count', 'Title']]
    
#     # Prepare data for the second line plot
#     line_plot_data = sorted_df.head(10)[['View Count', 'Like Count', 'Title']]
    
#     return {
#         'bar_plot_data': bar_plot_data.to_dict(orient='records'),
#         'line_plot_data': line_plot_data.to_dict(orient='records')
#     }


def process_videostats(data):
    df = pd.DataFrame(data)
    df.rename(columns={
        "video_stats_id": "index",
        "vid_id": "Video_ID",
        "date": "Date",
        "vid_title": "Title",
        "vid_view_cnt": "View_Count",
        "vid_like_cnt": "Like_Count",
        "vid_comment_cnt": "Comment_Count",
        "category": "Category",
        "channel": "Channel_ID"
    }, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Week'] = df['Date'].dt.strftime('%Y-%U')
    df['Month'] = df['Date'].dt.to_period('M')
    videos_per_week = df.groupby('Week')['Category'].count().reset_index()
    videos_per_month = df.groupby('Month')['Category'].count().reset_index()
    videos_per_month['Month'] = videos_per_month['Month'].astype(str)
    

    # Calculate Engagement Rate
    df['Engagement_Rate'] = (df['Like_Count'] + df['Comment_Count']) / df['View_Count']
    
    # Sort DataFrame by 'View Count' in descending order
    sorted_df = df.sort_values(by='View_Count', ascending=False)
    
    # Prepare data for the first bar plot
    bar_plot_data = sorted_df.head(10)[['View_Count', 'Title']]
    
    # Prepare data for the second line plot
    line_plot_data = sorted_df.head(10)[['View_Count', 'Like_Count', 'Title']]
    
    combined_response = {
        'Latest_20_videos': data,
        'videos_per_week': videos_per_week.to_dict(orient='records'),
        'videos_per_month': videos_per_month.to_dict(orient='records'),        
        'bar_plot_data': bar_plot_data.to_dict(orient='records'),
        'line_plot_data': line_plot_data.to_dict(orient='records')
    }
    return combined_response
