#!/usr/bin/python3
"""
Console Module
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            objects = models.storage.all()
            key = args[0] + "." + args[1]
            print(objects[key])
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            objects = models.storage.all()
            key = args[0] + "." + args[1]
            del objects[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = models.storage.all()
        if arg:
            try:
                objs = [str(obj) for obj in objects.values() if obj.__class__.__name__ == arg]
                print(objs)
                return
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            objects = models.storage.all()
            key = args[0] + "." + args[1]
            obj = objects[key]
            setattr(obj, args[2], args[3])
            models.storage.save()
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

    def default(self, line):
        """Default behavior"""
        commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        cmd = line.split(".")
        if len(cmd) == 2:
            command, args = cmd
            if command in commands:
                commands[command](args)
            elif command == "count":
                args = cmd[1].split('"')[0]
                objects = models.storage.all()
                count = sum(1 for obj in objects.values() if obj.__class__.__name__ == args)
                print(count)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()

