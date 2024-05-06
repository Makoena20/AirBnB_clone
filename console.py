#!/usr/bin/python3
"""
Module for the HBNBCommand class.
"""
import cmd
import json
import models


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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class_name>]
        """
        args = arg.split()
        if args and args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        models.storage.save()

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.
        Usage: count <class_name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in models.storage.all().values()
                    if type(obj).__name__ == args[0])
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

