#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program gracefully at end of file.
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Called when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

