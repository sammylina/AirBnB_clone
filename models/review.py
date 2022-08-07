#!/usr/bin/python3
"""
    module for Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        Class for Review
    """
    place_id = ""
    user_id = ""
    text = ""
