#!/usr/bin/python3
"""
Module contains class Rectangle

2. Inherits from Base
3. Add validation of all setter methods and instantiation (id excluded)
4. Add public method `def area(self):` which returns the area of Rectangle
5. Add he public method def `display(self):` which prints to stdout using #
6. Override the __str__ method so that it returns:
    [Rectangle] (<id>) <x>/<y> - <width>/<height>
7. Improve the public method `def display(self):`, consider x and y
8. Add the public method `def update(self, *args):` that assigns an argument
    to each attribute
9. Update `def update(self, *args):` to `update(self, *args, **kwargs):`
    which assigns a key/value argument to attributes
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle; inherits from class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """ displays a rectangle using # to stdout """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """ returns an “informal” string representation of an instance """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)
        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """ assign an argument/key-value argument to each attribute """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
