#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        # Implement create command logic here
        pass

    def do_show(self, arg):
        # Implement show command logic here
        pass

    def do_destroy(self, arg):
        # Implement destroy command logic here
        pass

    def do_all(self, arg):
        # Implement all command logic here
        pass

    def do_update(self, arg):
        # Implement update command logic here
        pass

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
