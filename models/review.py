#!/usr/bin/env python3
"""
This module defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method.
        """
        super().__init__(*args, **kwargs)
EOF

