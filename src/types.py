from enum import Enum
from datetime import datetime
from dataclasses import dataclass


class CommentCategory(Enum):
    CORRECTION = 0
    GRATUITOUS = 1
    HUMOROUS = 2
    UNRELATED = 3
    MISC = 4


class VideoCategory(Enum):
    PYTHON = 0
    XGBOOST = 1
    
    
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