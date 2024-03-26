#!/usr/bin/python3
"""
Console module for HBNB project.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line should not execute anything
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            del(storage.all()[key])
            storage.save()
        except Exception:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        try:
            if not arg:
                objects = storage.all()
            else:
                if arg not in storage.classes():
                    print("** class doesn't exist **")
                    return
                objects = storage.all(arg)
            print([str(obj) for obj in objects.values()])
        except Exception:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            obj = storage.all()[key]
            setattr(obj, args[2], args[3][1:-1])
            obj.save()
        except Exception:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

