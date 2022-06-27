# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import json
import os
from enum import Enum

from dataclasses import dataclass

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

URL = "https://youtube.googleapis.com/youtube/v3/comments/"
BASE_URL = "https://www.googleapis.com/youtube/v3/"
API_KEY = "AIzaSyB5mcbaxQsh3wod3jod2i-Ba4vBVCaSy28"
HEADERS = {"Accept": "application/json"}


class CommentCategory(Enum):
    pass
@dataclass
class VideoData:
    """For videos, catagory will be either 'xgboost' or 'python'"""
    id: str
    title: str
    published_at_dt: datetime
    category: str
    
    
@dataclass
class CommentData:
    """For comments, category will be one of the enumerated types."""
    id: str
    text: str
    published_at_dt: datetime
    updated_at_dt: datetime
    age_dt: datetime
    like_count: int
    complexity: int
    sentiment: int
    category: str


    
def search_by_keyword(keyword) -> dict:
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.search().list(
        part="snippet", channelType="any", maxResults=25, q=keyword
    )
    response = request.execute()

    for item in response["items"]:
        print(item["etag"])

    return [item for item in response["items"]]


def sanitize_string(string):
    return string.replace(",","").replace("\"","").replace("\n","").replace("\t","")


def extract_comments(search_term):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    video_request = youtube.search().list(
        part="snippet", channelType="any", maxResults=25, q=search_term
    )
    response = video_request.execute()
    video_items = [item for item in response["items"]]

    file_name = f"{search_term.split()[0]}_comments_sanitized.csv"
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )

        for item in video_items:
            video_id = item["id"]["videoId"]
            video_title = sanitize_string(item["snippet"]["title"])
            video_published_datetime = item["snippet"]["publishedAt"]

            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id
            )
            response = request.execute()
            for response_item in response["items"]:
                comment = response_item["snippet"]["topLevelComment"]["snippet"]
                comment_text = sanitize_string(comment["textOriginal"].strip())
                comment_published_at = comment["publishedAt"]
                comment_updated_at = comment["updatedAt"]
                comment_like_count = comment["likeCount"]
                writer.writerow(
                    [
                        video_id,
                        video_title,
                        video_published_datetime,
                        comment_text,
                        comment_published_at,
                        comment_updated_at,
                        comment_like_count,
                    ]
                )

if __name__ == "__main__":
    #search_by_keyword("")
    # extract_comments("python tutorial")
    extract_comments("xgboost python tutorial")
