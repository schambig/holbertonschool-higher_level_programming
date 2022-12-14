#!/usr/bin/python3
"""
Module contains class Square

10. Inherits from Rectangle
11. Add the public getter and setter size
12. Add the public method `def update(self, *args, **kwargs):`
    that assigns attributes
14. Add the public method `def to_dictionary(self):`
    that returns the dictionary representation of a Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square; inherits from class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns an “informal” string representation of an instance """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)
        return str_square + str_id + str_xy + str_size

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.heigt = value

    def update(self, *args, **kwargs):
        """ assign an argument/key-value argument to each attribute """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        list_atr = ['id', 'size', 'x', 'y']
        dict_rep = {}

        for key in list_atr:
            if key == 'size':
                dict_rep[key] = getattr(self, 'width')
            else:
                dict_rep[key] = getattr(self, key)
        return dict_rep
