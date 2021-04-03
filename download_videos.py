from __future__ import unicode_literals

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import youtube_dl

api_service_name = "youtube"
api_version = "v3"
developer_key = "not an api key"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=developer_key)
request = youtube.search().list(
    part="id,snippet",
    q="nu metal official video after:2009-01-01 before:2010-01-01",
    type="video",
    videoDefinition="standard",
    maxResults=50
)
response = request.execute()
    
print(response)
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for search_result in response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            vid = search_result['id']['videoId']
            ydl.download(["https://www.youtube.com/watch?v=" + vid])
