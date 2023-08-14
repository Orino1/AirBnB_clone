#!/usr/bin/python3
"""
A basic command interpreter model.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    A basic command interpreter class.
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User }

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
        if arg not in HBNBCommand.classes:
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
            if args[0] not in HBNBCommand.classes:
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
            print("** instance id missing **")
            return
        if len(args) == 2:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
                return
            else:
                print("** no instance found **")

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
        args = arg.split(' ')
        if len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    if args[0] in key:
                        list_of_models.append(str(value))
                print(list_of_models)

    def do_update(self, arg):
        """
        Update instance attributes.
        
        Usage: update <class> <id> <attr> <value>
        
        Errors:
        - Missing class name: ** class name missing **
        - Unknown class: ** class doesn't exist **
        - Missing instance id: ** instance id missing **
        - Missing attribute name: ** attribute name missing **
        - Instance not found: ** no instance found **
        - Missing value: ** value missing **
        
        Example: update BaseModel 1234-5678-9012 name "John"
        """
        if arg == '':
            print("** class name missing **")
            return
        args = arg.split(' ')
        # THIS IS JUST A HACK
        if len(args) == 1:
            if args[0] in HBNBCommand.classes:
                print("** instance id missing **")
                return
            else:
                print("** class doesn't exist **")
                return
        if len(args) == 2:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print("** attribute name missing **")
                return
            else:
                print("** no instance found **")
                return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) > 3:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
                return
            if '"' in args[3]:
                args[3] = args[3].strip('"')
            # Im assuming that "" mean a string 
            # float or int otherwise
            else:
                if "." in args[3]:
                    args[3] = float(args[3])
                else:
                    args[3] = int(args[3])
            # I dont know what attributes should i convert the data for
            storage.all()[key].args[2] = args[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
