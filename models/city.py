#!/usr/bin/env python3
"""Module defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel."""

    state_id = ""
    name = ""
