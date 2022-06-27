```python
# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        channelType="any",
        maxResults=25,
        q="xgboost tutorial"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
```


```json
{
  "kind": "youtube#searchListResponse",
  "etag": "QYccTjrkC8IzeLPST2Kh40r_Tzk",
  "nextPageToken": "CBkQAA",
  "regionCode": "US",
  "pageInfo": {
    "totalResults": 31235,
    "resultsPerPage": 25
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "FbHYug_rrCw2eSTglJA_MayS-Fo",
      "id": {
        "kind": "youtube#video",
        "videoId": "GrJP9FLV3FE"
      },
      "snippet": {
        "publishedAt": "2020-08-01T18:13:06Z",
        "channelId": "UCtYLUTtgS3k1Fg4y5tAhLbw",
        "title": "XGBoost in Python from Start to Finish",
        "description": "NOTE: You can support StatQuest by purchasing the Jupyter Notebook and Python code seen in this video here: ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/GrJP9FLV3FE/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/GrJP9FLV3FE/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/GrJP9FLV3FE/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "StatQuest with Josh Starmer",
        "liveBroadcastContent": "none",
        "publishTime": "2020-08-01T18:13:06Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "YHlvFGPFAT1iZ2su7wMeCjTc72s",
      "id": {
        "kind": "youtube#video",
        "videoId": "OtD8wVaFm6E"
      },
      "snippet": {
        "publishedAt": "2019-12-16T14:00:04Z",
        "channelId": "UCtYLUTtgS3k1Fg4y5tAhLbw",
        "title": "XGBoost Part 1 (of 4): Regression",
        "description": "XGBoost is an extreme machine learning algorithm, and that means it's got lots of parts. In this video, we focus on the unique ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/OtD8wVaFm6E/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/OtD8wVaFm6E/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/OtD8wVaFm6E/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "StatQuest with Josh Starmer",
        "liveBroadcastContent": "none",
        "publishTime": "2019-12-16T14:00:04Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "8wAFAc2MA3WsKs760tYoGuk-sJc",
      "id": {
        "kind": "youtube#video",
        "videoId": "ap2SS0-XPcE"
      },
      "snippet": {
        "publishedAt": "2021-05-17T15:43:40Z",
        "channelId": "UCueeXkuJezkCqu0YryvJnnQ",
        "title": "XGBoost Model in Python | Tutorial | Machine Learning",
        "description": "How to create a classification model using XGBoost in Python? The tutorial will provide a step-by-step guide for this. Problem ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/ap2SS0-XPcE/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/ap2SS0-XPcE/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/ap2SS0-XPcE/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Harsh Kumar",
        "liveBroadcastContent": "none",
        "publishTime": "2021-05-17T15:43:40Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "d7xUas40sNJEpxzpf-0r-_EbK08",
      "id": {
        "kind": "youtube#video",
        "videoId": "OQKQHNCVf5k"
      },
      "snippet": {
        "publishedAt": "2020-02-11T21:07:51Z",
        "channelId": "UC40lkNGGObJc9hEGmFTQbrQ",
        "title": "XGBoost: How it works, with an example.",
        "description": "In this excerpt, we cover perhaps the most powerful machine learning algorithm today: XGBoost (eXtreme Gradient Boosted trees) ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/OQKQHNCVf5k/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/OQKQHNCVf5k/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/OQKQHNCVf5k/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Sundog Education with Frank Kane",
        "liveBroadcastContent": "none",
        "publishTime": "2020-02-11T21:07:51Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "CRSVASq4dpog4nKhrFO0NpvbJG0",
      "id": {
        "kind": "youtube#video",
        "videoId": "Y7uNT0alrKk"
      },
      "snippet": {
        "publishedAt": "2020-08-14T15:46:55Z",
        "channelId": "UCDia_lkNYKLJVLRLQl_-pFw",
        "title": "Complete Beginners Guide to XGBoost Models",
        "description": "Frank Kane, Sundog Education founder and the author of liveVideo course Machine Learning, Data Science and Deep ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Y7uNT0alrKk/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Y7uNT0alrKk/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Y7uNT0alrKk/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Manning Publications",
        "liveBroadcastContent": "none",
        "publishTime": "2020-08-14T15:46:55Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "Q_-Bzk0aiPgwZ_8agDyczby0rko",
      "id": {
        "kind": "youtube#video",
        "videoId": "gUJVmds9DsI"
      },
      "snippet": {
        "publishedAt": "2020-04-12T06:36:46Z",
        "channelId": "UC79Gv3mYp6zKiSwYemEik9A",
        "title": "Python Tutorial : Introducing XGBoost",
        "description": "Want to learn more? Take the full course at https://learn.datacamp.com/courses/extreme-gradient-boosting-with-xgboost at your ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/gUJVmds9DsI/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/gUJVmds9DsI/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/gUJVmds9DsI/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "DataCamp",
        "liveBroadcastContent": "none",
        "publishTime": "2020-04-12T06:36:46Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "9RrdoklfXwLcqRJjwcH85u0Ksf0",
      "id": {
        "kind": "youtube#video",
        "videoId": "VgDe0gwesrw"
      },
      "snippet": {
        "publishedAt": "2020-04-09T02:17:17Z",
        "channelId": "UC79Gv3mYp6zKiSwYemEik9A",
        "title": "Python Tutorial : When should I use XGBoost?",
        "description": "Want to learn more? Take the full course at https://learn.datacamp.com/courses/extreme-gradient-boosting-with-xgboost at your ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/VgDe0gwesrw/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/VgDe0gwesrw/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/VgDe0gwesrw/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "DataCamp",
        "liveBroadcastContent": "none",
        "publishTime": "2020-04-09T02:17:17Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "wKbkx6be7SpchRLpiuJHWMQWTcA",
      "id": {
        "kind": "youtube#video",
        "videoId": "kho6oANGu_A"
      },
      "snippet": {
        "publishedAt": "2019-06-27T14:19:35Z",
        "channelId": "UCkw4JCwteGrDHIsyIIKo4tQ",
        "title": "Boosting Machine Learning Tutorial | Adaptive Boosting, Gradient Boosting, XGBoost | Edureka",
        "description": "Machine Learning Certification Training using Python: https://www.edureka.co/python ** This Edureka session will help you ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/kho6oANGu_A/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/kho6oANGu_A/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/kho6oANGu_A/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "edureka!",
        "liveBroadcastContent": "none",
        "publishTime": "2019-06-27T14:19:35Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "NnrGq4arzltRzrk4m96cL8o32uM",
      "id": {
        "kind": "youtube#video",
        "videoId": "PxgVFp5a0E4"
      },
      "snippet": {
        "publishedAt": "2021-02-28T18:15:08Z",
        "channelId": "UC76VWNgXnU6z0RSPGwSkNIg",
        "title": "XGBoost Made Easy | Extreme Gradient Boosting | AWS SageMaker",
        "description": "Recently, XGBoost is the go to algorithm for most developers and has won several Kaggle competitions. Since the technique is an ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/PxgVFp5a0E4/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/PxgVFp5a0E4/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/PxgVFp5a0E4/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Professor Ryan",
        "liveBroadcastContent": "none",
        "publishTime": "2021-02-28T18:15:08Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "VDMjob04Th1p2LEebIDL4kDY3Us",
      "id": {
        "kind": "youtube#video",
        "videoId": "gPciUPwWJQQ"
      },
      "snippet": {
        "publishedAt": "2020-10-12T16:01:17Z",
        "channelId": "UCNU_lfiiWBdtULKOw6X0Dig",
        "title": "Xgboost Classification Indepth Maths Intuition- Machine Learning Algorithms🔥🔥🔥🔥",
        "description": "XGBoost is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting framework. In prediction ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/gPciUPwWJQQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/gPciUPwWJQQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/gPciUPwWJQQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Krish Naik",
        "liveBroadcastContent": "none",
        "publishTime": "2020-10-12T16:01:17Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "OU-jgr6uN4VgRApzSSatTcWgmV8",
      "id": {
        "kind": "youtube#video",
        "videoId": "AvWfL1Us3Kg"
      },
      "snippet": {
        "publishedAt": "2019-12-31T11:55:04Z",
        "channelId": "UCpbMQO3wyA-vfYiCiIGB8Iw",
        "title": "XGBOOST in Python (Hyper parameter tuning)",
        "description": "Trainer: Mr. Ashok Veda - https://in.linkedin.com/in/ashokveda XGBoost is one of algorithms that has recently been dominating ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/AvWfL1Us3Kg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/AvWfL1Us3Kg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/AvWfL1Us3Kg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "DataMites",
        "liveBroadcastContent": "none",
        "publishTime": "2019-12-31T11:55:04Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "tnVlp2hCsJlpv8OiNxpVVKdXWAA",
      "id": {
        "kind": "youtube#video",
        "videoId": "rMeq9khzdvM"
      },
      "snippet": {
        "publishedAt": "2020-12-15T20:28:35Z",
        "channelId": "UCzo2A1KivHp5dBh1jzB6TyQ",
        "title": "Practical Machine learning Tutorial : XGBoost implementation in Python",
        "description": "I have practically shown how to implement the XGBoost model in Python using sklearn API.",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/rMeq9khzdvM/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/rMeq9khzdvM/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/rMeq9khzdvM/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Technology Sensei",
        "liveBroadcastContent": "none",
        "publishTime": "2020-12-15T20:28:35Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "Txj-a4npdO8sN8Kswv-Bd9cCAnY",
      "id": {
        "kind": "youtube#video",
        "videoId": "wO7YBNPCu58"
      },
      "snippet": {
        "publishedAt": "2020-04-09T02:09:36Z",
        "channelId": "UC79Gv3mYp6zKiSwYemEik9A",
        "title": "Python Tutorial : Extreme Gradient Boosting with XGBoost",
        "description": "Want to learn more? Take the full course at https://learn.datacamp.com/courses/extreme-gradient-boosting-with-xgboost at your ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/wO7YBNPCu58/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/wO7YBNPCu58/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/wO7YBNPCu58/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "DataCamp",
        "liveBroadcastContent": "none",
        "publishTime": "2020-04-09T02:09:36Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "hEtYroKz-yHi1F5NnyV54LFq1cc",
      "id": {
        "kind": "youtube#video",
        "videoId": "87xRqEAx6CY"
      },
      "snippet": {
        "publishedAt": "2016-02-10T02:40:57Z",
        "channelId": "UCbjfaADRqnNvebxbxlrU3mg",
        "title": "xgboost tutorial",
        "description": "Extreme gradient boosting for trees: This machine learning algorithm is in my opinion better than random Forest on AVERAGE.",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/87xRqEAx6CY/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/87xRqEAx6CY/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/87xRqEAx6CY/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "The Math Student",
        "liveBroadcastContent": "none",
        "publishTime": "2016-02-10T02:40:57Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "u8Kk-QADtHg5p4R7OEgHNILvXjA",
      "id": {
        "kind": "youtube#video",
        "videoId": "TyvYZ26alZs"
      },
      "snippet": {
        "publishedAt": "2020-10-10T17:07:04Z",
        "channelId": "UCXzz7hebK1NYIKaXyaKXmQA",
        "title": "Visual Guide to Gradient Boosted Trees (xgboost)",
        "description": "Gradient Boosted Trees are everywhere! They're very powerful ensembles of Decision Trees that rival the power of Deep ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/TyvYZ26alZs/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/TyvYZ26alZs/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/TyvYZ26alZs/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Econoscent",
        "liveBroadcastContent": "none",
        "publishTime": "2020-10-10T17:07:04Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "k9R7FLgIVJ-fgqWzuXt5y900BoA",
      "id": {
        "kind": "youtube#video",
        "videoId": "0ikyjpaUDFQ"
      },
      "snippet": {
        "publishedAt": "2021-08-26T15:30:00Z",
        "channelId": "UCtxCXg-UvSnTKPOzLH4wJaQ",
        "title": "Intro to XGBoost Models (decision-tree-based ensemble ML algorithms)",
        "description": "Frank Kane, Sundog Education founder and the author of liveVideo course Machine Learning, Data Science and Deep ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/0ikyjpaUDFQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/0ikyjpaUDFQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/0ikyjpaUDFQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Coding Tech",
        "liveBroadcastContent": "none",
        "publishTime": "2021-08-26T15:30:00Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "rt96wuFkTPzislTtpzBKgYBkoUo",
      "id": {
        "kind": "youtube#video",
        "videoId": "8b1JEDvenQU"
      },
      "snippet": {
        "publishedAt": "2020-01-13T12:30:01Z",
        "channelId": "UCtYLUTtgS3k1Fg4y5tAhLbw",
        "title": "XGBoost Part 2 (of 4): Classification",
        "description": "In this video we pick up where we left off in part 1 and cover how XGBoost trees are built for Classification. NOTE: This StatQuest ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/8b1JEDvenQU/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/8b1JEDvenQU/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/8b1JEDvenQU/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "StatQuest with Josh Starmer",
        "liveBroadcastContent": "none",
        "publishTime": "2020-01-13T12:30:01Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "aX7OaL1WoD40SpN0oO239ZMK0vA",
      "id": {
        "kind": "youtube#video",
        "videoId": "UEKNMFKxK0M"
      },
      "snippet": {
        "publishedAt": "2021-07-17T15:30:11Z",
        "channelId": "UCmKaoNn0OvxVAe7f_8sXYNQ",
        "title": "Gradient Boosting with XGBoost (5/6) | Machine Learning with Python: Zero to GBMs",
        "description": "Lecture 5 of the Machine Learning with Python: Zero to GBMs course. In this lesson, you will download a real-world dataset from a ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/UEKNMFKxK0M/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/UEKNMFKxK0M/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/UEKNMFKxK0M/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Jovian",
        "liveBroadcastContent": "none",
        "publishTime": "2021-07-17T15:30:11Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "r3UYiFkAjsXHnCwP6jNyZg-5Rbo",
      "id": {
        "kind": "youtube#video",
        "videoId": "iBSMdFJ6Iqc"
      },
      "snippet": {
        "publishedAt": "2020-07-21T23:19:00Z",
        "channelId": "UCS1dQr2X_ComHN4PXYDS4gA",
        "title": "XGBOOST Math Explained - Objective function derivation &amp; Tree Growing | Step By Step",
        "description": "XGBOOST Math explained clearly step by step - The Objective function derivation along with Tree Growing. Get ready for your ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/iBSMdFJ6Iqc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/iBSMdFJ6Iqc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/iBSMdFJ6Iqc/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Machine Learning Mastery",
        "liveBroadcastContent": "none",
        "publishTime": "2020-07-21T23:19:00Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "xHBMCj_upD1s0lLo92P_M9F9Hlo",
      "id": {
        "kind": "youtube#video",
        "videoId": "f3ryHJ05h5k"
      },
      "snippet": {
        "publishedAt": "2020-03-30T12:48:03Z",
        "channelId": "UCEa753oV5uDIuWgyLVIqt4w",
        "title": "贪心学院xgboost细节讲解录播，目前为止听过最全最细致的讲解",
        "description": "xgboost.",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/f3ryHJ05h5k/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/f3ryHJ05h5k/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/f3ryHJ05h5k/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "yong deng",
        "liveBroadcastContent": "none",
        "publishTime": "2020-03-30T12:48:03Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "H8As7WMwHmiz82GesFpT7GEks3Y",
      "id": {
        "kind": "youtube#video",
        "videoId": "vZuObCbSRQg"
      },
      "snippet": {
        "publishedAt": "2021-11-16T19:50:19Z",
        "channelId": "UC79Gv3mYp6zKiSwYemEik9A",
        "title": "Live Code Along: Machine Learning with XGBoost in Python",
        "description": "During this code-along, Lis Sulmont, Workspace Architect at DataCamp, will use XGBoost to predict booking cancellations with ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/vZuObCbSRQg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/vZuObCbSRQg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/vZuObCbSRQg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "DataCamp",
        "liveBroadcastContent": "none",
        "publishTime": "2021-11-16T19:50:19Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "if6KgGzKs_ZJFJzYD4FN77TziNY",
      "id": {
        "kind": "youtube#video",
        "videoId": "Amx3kx3iAaM"
      },
      "snippet": {
        "publishedAt": "2020-07-20T22:00:05Z",
        "channelId": "UCAKtTBXNwRJ_EHGq0EbwokQ",
        "title": "XGBoost tutorial in Python",
        "description": "To access my secret discount portal: https://linktr.ee/diogoalvesderesende New course on Zero To Mastery Academy: ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Amx3kx3iAaM/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Amx3kx3iAaM/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Amx3kx3iAaM/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Data Heroes",
        "liveBroadcastContent": "none",
        "publishTime": "2020-07-20T22:00:05Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "pLaLWO9fxQpwIeanFOXzrQ_SKG0",
      "id": {
        "kind": "youtube#video",
        "videoId": "gKyUucJwD8U"
      },
      "snippet": {
        "publishedAt": "2020-08-16T17:54:08Z",
        "channelId": "UCAKtTBXNwRJ_EHGq0EbwokQ",
        "title": "XGBoost tutorial in R",
        "description": "To access my secret discount portal: https://linktr.ee/diogoalvesderesende New course on Zero To Mastery Academy: ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/gKyUucJwD8U/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/gKyUucJwD8U/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/gKyUucJwD8U/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Data Heroes",
        "liveBroadcastContent": "none",
        "publishTime": "2020-08-16T17:54:08Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "V-AEuEzQuiOkY-7H5pG_PsLzqg0",
      "id": {
        "kind": "youtube#video",
        "videoId": "_e0NFIaHY2c"
      },
      "snippet": {
        "publishedAt": "2021-07-29T23:53:09Z",
        "channelId": "UCTTBgWyJl2HrrhQOOc710kA",
        "title": "Tune xgboost more efficiently with racing methods",
        "description": "In this screencast, I use data on baseball home runs from the recent episode of #SLICED to build an xgboost model, and tune ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/_e0NFIaHY2c/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/_e0NFIaHY2c/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/_e0NFIaHY2c/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Julia Silge",
        "liveBroadcastContent": "none",
        "publishTime": "2021-07-29T23:53:09Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "GUiMl-WsZqIC267C-uh3giHiBCk",
      "id": {
        "kind": "youtube#video",
        "videoId": "woVTNwRrFHE"
      },
      "snippet": {
        "publishedAt": "2017-10-29T13:34:53Z",
        "channelId": "UCuWECsa_za4gm7B3TLgeV_A",
        "title": "eXtreme Gradient Boosting XGBoost Algorithm with R - Example in Easy Steps with One-Hot Encoding",
        "description": "Provides easy to apply example of eXtreme Gradient Boosting XGBoost Algorithm with R . Data file and R code: ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/woVTNwRrFHE/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/woVTNwRrFHE/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/woVTNwRrFHE/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Dr. Bharatendra Rai",
        "liveBroadcastContent": "none",
        "publishTime": "2017-10-29T13:34:53Z"
      }
    }
  ]
}
```