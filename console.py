#!/usr/bin/python3
"""
Module for the HBNBCommand class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def help_quit(self):
        """
        Quit command to exit the program
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Exit the program
        """
        print("Exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

