#!/usr/bin/python3
"""
Module console
contains the entry point to the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """ Interprets Ctrl + D
        """

        print()
        return True

    def emptyline(self):
        """nothing excuted when Enter is pressed"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
