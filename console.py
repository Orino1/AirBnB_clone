#!/usr/bin/python3
<<<<<<< HEAD
import cmd
"""
comsole mdule

"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    def __init__(self, prompt='(hbnb) '):
        """making the prompt = '(hbnb) '"""
        super().__init__()
        self.prompt = prompt

    def do_quit(self, args):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, args):
        """EOF command to exit the program"""
        exit()
=======
"""
A basic command interpreter model.
"""
import cmd


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

>>>>>>> refs/remotes/origin/master

if __name__ == '__main__':
    HBNBCommand().cmdloop()
