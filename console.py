#!/usr/bin/python3
"""
Module console
contains the entry point to the command interpreter
"""


import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']

    def do_quit(self, line):
        """ Quit command to exit the program
        """

        return True

    def do_EOF(self, line):
        """ Interprets Ctrl + D
        """

        print()
        return True

    def emptyline(self):
        """nothing excuted when Enter is pressed"""

        pass

    def do_create(self, args):
        """ create instance of base model"""

        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
            return
        try:
            d = eval(arg_list[0] + '()')
            d.save()
            print(d.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id
        """

        arg_list = args.split()

        if validate(arg_list):
            obj_ref = validate(arg_list)
            all_instances = models.storage.all()

            if obj_ref in all_instances.keys():
                reference = all_instances[obj_ref]
                print(reference)
            else:
                print("** no instance found **")
                return

    def do_destroy(self, args):
        """
         Deletes an instance based on the class name and id
        """

        arg_list = args.split()

        if validate(arg_list):
            obj_reference = validate(arg_list)
            all_instances = models.storage.all()

            if obj_reference in all_instances.keys():
                del all_instances[obj_reference]
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name
        """

        instances = models.storage.all()
        if args:
            arg_list = args.split()
            print(arg_list[0])
            if arg_list[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                new_list = [str(instances[obj]) for obj in instances.keys()
                            if arg_list[0] in obj]
                print(new_list)
        else:
            new_list = [str(instances[obj]) for obj in instances.keys()]
            print(new_list)

    def do_update(self, args):
        """Update an specific dictionary based in the class name
            and the id reference
        """

        arg_list = args.split()
        if validate(args_list):
            obj_ref = validate(arg_list)
            all_instances = models.storage.all()

            if obj_ref in all_instances.keys():
                obj = all_instances[obj_ref]
                len_arg_list = len(arguments_list)

                if len_arg_list < 3:
                    print("** attribute name missing **")
                    return
                elif len_arg_list < 4:
                    print("** value missing **")
                    return
                else:
                    try:
                        value = int(arg_list[3].replace('"', ""))
                    except:
                        try:
                            value = float(arg_list[3].replace('"', ""))
                        except:
                            try:
                                value = str(arg_list[3].replace('"', ""))
                            except:
                                pass
                    obj.__dict__[arg_list[2]] = value
                    models.storage.save()
                    return
            else:
                print("** no instance found **")
                return

def validate(list_args):
        """Function to validate content in list or arguments
        """

        if list:
            len_list = len(list_args)
            if len_list < 1:
                print("** class name missing **")
                return None

            if (list_args[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
                return None

            if len_list < 2:
                print("** instance id missing **")
                return None

            obj_reference = list_args[0] + '.' + list_args[1]
            return    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
