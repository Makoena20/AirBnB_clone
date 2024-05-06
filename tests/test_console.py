#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test cases for console.py"""

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue().strip())

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual('', f.getvalue().strip())

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn('quit', f.getvalue())

    def test_empty_line(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue().strip())

    def test_create_BaseModel(self):
        """Test create BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            # Add assertions here

    # Add more test cases for other functionalities


if __name__ == '__main__':
    unittest.main()

