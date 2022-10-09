#!/usr/bin/python3
"""
Module contains class Square

10. Inherits from Rectangle
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
        str_wh = "{}/{}".format(self.width, self.height)
        return str_square + str_id + str_xy + str_wh
