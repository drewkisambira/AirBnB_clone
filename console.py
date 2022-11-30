#!/usr/bin/python3
"""
Module console
contains the entry point to the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ Interprets Ctrl + D
        """

        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program
        """

        raise SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
