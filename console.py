#!/usr/bin/python3

"""
    module for command interpreter tool
"""

import re
import cmd
import models


def pattern(arg):
    """Changes the default input function to manage callable functions"""
    pattern = '\.([^.]+)\(|([^(),]+)[,\s()]*[,\s()]*'
    arguments = re.findall(pattern, arg)
    cmd = arguments[0][0]
    arguments = arguments[1:]
    line = ' '.join(map(lambda x: x[1].strip('"'), arguments))
    return cmd, line

def loop_dict(line, obj_update):
    """Loopinf function for advanced tasks"""
    idx = 4
    while idx <= len(line):
        try:
            attr = line[idx]
        except IndexError:
            print("** attribute name missing **")
        else:
            try:
                val = line[idx + 1]
            except IndexError:
                print("** no value found **")
            else:
                setattr(obj_update, attr, val)
                obj_update.save()
                if idx + 1 == len(line) - 1:
                    break
        idx += 1

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

    def do_count(self, argv):
        """Counts the number of instances of a class"""
        instance_cnt = 0
        curr_dict = models.storage.all()
        for key, val in curr_dict.items():
            val = val.to_dict()
            if val['__class__'] == argv:
                instance_cnt += 1
        print(instance_cnt)

    def do_Amenity(self, arg):
        """ helper function for amenity class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Amenity', line]))

    def do_User(self, arg):
        """ Helper function for User class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'User', line]))

    def do_BaseModel(self, arg):
        """ Helper function for BaseModel Class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'BaseModel', line]))

    def do_City(self, arg):
        """ Helper function for BaseModel Class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'City', line]))

    def do_Review(self, arg):
        """ Helper function for Review class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Review', line]))

    def do_State(self, arg):
        """ Helper function for State class """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'State', line]))

    def do_Place(self, arg):
        """ Helper function for Place class"""
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Place', line]))

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
