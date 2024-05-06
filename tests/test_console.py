#!/usr/bin/python3
"""
Unit tests for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
import console


class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNBCommand class methods
    """

    def test_help(self):
        """
        Test help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_quit(self):
        """
        Test quit command
        """
        with self.assertRaises(SystemExit):
            console.HBNBCommand().onecmd("quit")

    def test_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show(self):
        """
        Test show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_destroy(self):
        """
        Test destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_all(self):
        """
        Test all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("all")
            self.assertIn("*** No instances found ***", f.getvalue())

    def test_update(self):
        """
        Test update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())


if __name__ == '__main__':
    unittest.main()

