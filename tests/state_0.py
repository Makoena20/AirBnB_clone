#!/usr/bin/python3
"""Test for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def test_instance_creation(self):
        """Test instance creation"""
        state = State()
        self.assertIsInstance(state, State)


if __name__ == "__main__":
    unittest.main()

