#!/usr/bin/env python3
"""Module for the HBNB command interpreter."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()






#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import sys
import json
import models

classes = {"BaseModel": models.BaseModel}

class Console(cmd.Cmd):
    """
    Console class for command interpreter.
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            instance = classes[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if arg in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt.
        """
        pass

    def do_EOF(self, line):
        """
        Method to handle the EOF (Ctrl+D) condition.
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

