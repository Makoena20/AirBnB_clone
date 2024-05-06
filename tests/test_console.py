#!/usr/bin/python3
"""
Unittest for the console.py file
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNBCommand class
    """

    def test_help_command(self):
        """
        Test the help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("EOF", output)
            self.assertIn("quit", output)
            self.assertIn("create", output)
            self.assertIn("show", output)
            self.assertIn("destroy", output)
            self.assertIn("all", output)
            self.assertIn("update", output)
            self.assertIn("count", output)

    def test_help_show_command(self):
        """
        Test the help show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("Usage: show <class> <id>", output)

    def test_help_create_command(self):
        """
        Test the help create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIn("Usage: create <class>", output)

    def test_help_destroy_command(self):
        """
        Test the help destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIn("Usage: destroy <class> <id>", output)

    def test_help_all_command(self):
        """
        Test the help all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIn("Usage: all <class>", output)

    def test_help_update_command(self):
        """
        Test the help update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIn("Usage: update <class> <id> <attribute_name> <attribute_value>", output)

    def test_help_count_command(self):
        """
        Test the help count command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            output = f.getvalue().strip()
            self.assertIn("Usage: count <class>", output)

    def test_quit_command(self):
        """
        Test the quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual("", output)

    def test_EOF_command(self):
        """
        Test the EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual("", output)

    def test_all_base_model(self):
        """
        Test BaseModel.all() method is present
        """
        self.assertTrue(hasattr(HBNBCommand, "do_all"))

    def test_count_base_model(self):
        """
        Test BaseModel.count() method is present
        """
        self.assertTrue(hasattr(HBNBCommand, "do_count"))

    # More tests for other classes and methods can be added similarly

if __name__ == '__main__':
    unittest.main()

