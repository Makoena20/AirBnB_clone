#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual(f.getvalue().strip(), "")

    # Repeat the above pattern for other commands such as "EOF", "help", etc.

    def test_create_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            # Assert the output of create command

    # Repeat the above pattern for other create commands such as "create User", "create State", etc.

    def test_show_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            # Assert the output of show command

    # Repeat the above pattern for other show commands such as "show User", "show State", etc.

    # Write tests for other functionalities like destroy, all, update, etc.

if __name__ == '__main__':
    unittest.main()

