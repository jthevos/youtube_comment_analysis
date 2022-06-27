# -*- coding: utf-8 -*-

import csv
import json
from nis import cat
import os
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from enum import Enum

import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv

import local_types
import local_utils as analysis


def extract_comments(search_term):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    api_service_name = os.getenv("API_SERIVCE_NAME") or "youtube"
    api_version = os.getenv("API_VERSION")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY
    )

    video_request = youtube.search().list(
        part="snippet", channelType="any", maxResults=25, q="xgboost python tutorial"
    )
    response = video_request.execute()
    video_items = [item for item in response["items"]]

    file_name = f"../data/{search_term.split()[0]}_comments_sanitized.csv"

    video_list = []
    comment_list = []
    for item in video_items:
        video_id = item["id"]["videoId"]
        video_list.append(
            local_types.VideoData(
                id=video_id,
                title=analysis.sanitize_string(item["snippet"]["title"]),
                published_at_dt=item["snippet"]["publishedAt"],
                category=local_types.VideoCategory.XGBOOST,
            )
        )

        request = youtube.commentThreads().list(
            part="snippet,replies", videoId=video_id
        )
        response = request.execute()
        for response_item in response["items"]:
            raw_comment = response_item["snippet"]["topLevelComment"]["snippet"]
            original_text = raw_comment["textOriginal"].strip()
            print(raw_comment["publishedAt"])
            comment_age_in_days = datetime.now() - datetime.fromisoformat(raw_comment["publishedAt"][:-1])
            # - timedelta(
            #     )
            # )  # Remove the timezone component

            # "publishedAt": "2022-06-14T21:29:00Z",
            comment_list.append(
                local_types.CommentData(
                    id=response_item["snippet"]["topLevelComment"]["id"],
                    text=analysis.sanitize_string(original_text),
                    published_at_dt=raw_comment["publishedAt"],
                    updated_at_dt=raw_comment["updatedAt"],
                    age_dt=comment_age_in_days,
                    like_count=raw_comment["likeCount"],
                    complexity=analysis.flesch_complexity(original_text),
                    sentiment=None,
                    category=None,
                )
            )

    print(video_list[0])
    print(comment_list[0])


if __name__ == "__main__":
    # extract_comments("python tutorial")

    # API_KEY = os.getenv("API_KEY")
    extract_comments("xgboost python tutorial")
