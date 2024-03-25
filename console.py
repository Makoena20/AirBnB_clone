#!/usr/bin/python3
"""
Console module for Airbnb clone project.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import shlex

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class, a subclass of cmd.Cmd for command interpreter.
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = FileStorage().all()
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (saves the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = FileStorage().all()
        if key in objs:
            del objs[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all.
        """
        objs = FileStorage().all()
        if arg:
            args = shlex.split(arg)
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            print([str(objs[key]) for key in objs.keys() if
                   key.startswith(args[0])])
        else:
            print([str(objs[key]) for key in objs.keys()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (saves the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = FileStorage().all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3])
        FileStorage().save()

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Overwrites emptyline method to prevent repeating the last non-empty
        command when the empty line is entered.
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()









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
