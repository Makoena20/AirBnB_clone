#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        print("create", arg)

    def do_show(self, arg):
        """Show the string representation of an instance"""
        print("show", arg)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        print("destroy", arg)

    def do_all(self, arg):
        """Print all string representations of all instances"""
        print("all", arg)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        print("update", arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

