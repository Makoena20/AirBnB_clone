#!/usr/bin/env python3
"""
This module defines the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method.
        """
        super().__init__(*args, **kwargs)
EOF
