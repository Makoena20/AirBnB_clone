#!/usr/bin/env python3
"""Module for HBNB console."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End-of-file(EOF) to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create new instance of BaseModel and save it."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.all():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])
        except KeyError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.all():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        objs = storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs])
            return
        try:
            if args[0] not in storage.all():
                print("** class doesn't exist **")
                return
            print([str(objs[obj]) for obj in objs if args[0] in obj])
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.all():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            obj = storage.all()[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        except KeyError:
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

