#!/usr/bin/python3

"""
    module for command interpreter tool
"""

import re
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
        class for command interpreter
    """

    prompt = '(hbnb) '

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it and prints the id
        """
        if len(argv) < 2:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict[argv]
            except KeyError:
                print("** class doesn't exist **")
            else:
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, argv):
        """Prints the string representation of an isntance based on \
                the class name and id
        """
        if len(argv) < 2:
            print("** class name missing **")
        else:
            argv = argv.split()
            if argv[0] in models.class_dict:
                try:
                    key = argv[0] + '.' + argv[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[key])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id, \
                saving the change to the json file
        """
        if len(argv) < 2:
            print("** class name missing **")
        else:
            argv = argv.split()
            if argv[0] in models.class_dict:
                try:
                    key = argv[0] + '.' + argv[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, argv):
        """Prints all string representation of all instances based or not \
                on the class name
        """
        if len(argv) == 0:
            print([str(v) for v in models.storage.all().values()])
        elif argv not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print(
                [str(v) for k, v in models.storage.all().items() if argv in k]
            )

    def do_update(self, argv):
        """Updates an instance based on the class name and id
        """
        if len(argv) == 0:
            print("** class name missing **")
        else:
            argv = argv.split(' ')
            for i in range(len(argv)):
                argv[i] = argv[i].strip("\"'\"{\"}:\"'")
            if argv[0] in models.class_dict:
                try:
                    obj_id = argv[0] + '.' + argv[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = argv[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = argv[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    val = argv[3]
                                except IndexError:
                                    print("** value missing **")
                                else:
                                    setattr(obj, attr, val)
                                    obj.save()
                                    if len(argv) >= 5:
                                        loop_dict(argv, obj)
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """
            empty line + ENTER shouldn't execute anything
        """
        pass

    def do_quit(self, argv):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, argv):
        """Press CTRL+d to force close the program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
