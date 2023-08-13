#!/usr/bin/python3
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
