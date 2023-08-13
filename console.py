#!/usr/bin/python3
"""
A basic command interpreter model.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A basic command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program (Ctrl-D).
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it (to the JSON file),
        and print the id.
        """
        if arg == "":
            print("** class name missing **")
            # Note_to_self: return save you from nested hell
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = eval(f"{arg}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        if arg == "":
            print("** class name missing **")
            return
        args = arg.split(' ')
        if len(args) == 2:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            obj_key = f"{args[0]}.{args[1]}"
            for key, value in storage.all().items():
                if obj_key in key:
                    # print to_dict() according to the example from main
                    # but not sure if they meant (__str__)
                    print(storage.all()[key])
                    return
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        if arg == "":
            print("** class name missing **")
            return
        args = arg.split(' ')
        if len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            key = f"{args[0]}.{args}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not on
        the class name.
        """
        list_of_models = []
        if arg == "":
            for key, value in storage.all().items():
                list_of_models.append(str(value))
            print(list_of_models)
            return
        args = arg.split()
        if len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    if args[0] in key:
                        list_of_models.append(str(value))
                print(list_of_models)

    def do_update(self, arg):
        """
        Not yet
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
