#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """hbnbcommand class"""
    def __init__(self, prompt='(hbnb) '):
        """init"""
        super().__init__()
        self.prompt = prompt

    def do_help(self, args):
        """displays help"""
        if args == "quit" or args == "EOF":
            print("Quit command to exit the program")
        else:
            print("EOF  help  quit")

    def do_quit(self, args):
        """quits shell"""
        exit()

    def do_EOF(self, args):
        """quits shell"""
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
