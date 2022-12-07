<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# Python Inheritance<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language, it has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class. This project covers the nuances of these concepts.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Resources<!--@schambig-->

Important concepts to help you understand this project:

* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://hub.packtpub.com/inheritance-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk) (Derek Banas video)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-lookup.py](0-lookup.py)</pre><!--@schambig--> | Write a function that returns the list of available attributes and methods of an object:<br>• Prototype: `def lookup(obj):`<br>• Returns a `list` object<br>• You are not allowed to import any module |
| <pre>[1-my_list.py](1-my_list.py)</pre><!--@schambig--> | Write a class `MyList` that inherits from `list`: <br>• Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)<br>• You can assume that all the elements of the list will be of type `int`<br>• You are not allowed to import any module |
| <pre>[2-is_same_class.py](2-is_same_class.py)</pre><!--@schambig--> | Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.<br>• Prototype: `def is_same_class(obj, a_class):`<br>• You are not allowed to import any module |
| <pre>[3-is_kind_of_class.py](3-is_kind_of_class.py)</pre><!--@schambig--> | Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.<br>• Prototype: `def is_kind_of_class(obj, a_class):`<br>• You are not allowed to import any module |
| <pre>[4-inherits_from.py](4-inherits_from.py)</pre><!--@schambig--> | Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.<br>• Prototype: `def inherits_from(obj, a_class):`<br>• You are not allowed to `import` any `modul`e |
| <pre>[5-base_geometry.py](5-base_geometry.py)</pre><!--@schambig--> | Write an empty class `BaseGeometry`.<br>• You are not allowed to import any module |
| <pre>[6-base_geometry.py](6-base_geometry.py)</pre><!--@schambig--> | Write a class `BaseGeometry` (based on `5-base_geometry.py`).<br>• Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`<br>• You are not allowed to import any module |
| <pre>[7-base_geometry.py](7-base_geometry.py)</pre><!--@schambig--> | Write a class `BaseGeometry` (based on `6-base_geometry.py`).<br>• Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`<br>• Public instance method: `def integer_validator(self, name, value):` that validates `value`:<br>• You are not allowed to import any module |
| <pre>[8-rectangle.py](8-rectangle.py)</pre><!--@schambig--> | Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).<br>• Instantiation with `width` and `height`: `def __init__(self, width, height):` |
| <pre>[9-rectangle.py](9-rectangle.py)</pre><!--@schambig--> | Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)<br>• Instantiation with `width` and `height`: `def __init__(self, width, height):`<br>• the `area()` method must be implemented<br>• `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>` |
| <pre>[10-square.py](10-square.py)</pre><!--@schambig--> | Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):<br>• Instantiation with size: `def __init__(self, size):`<br>• the `area()` method must be implemented | 
| <pre>[11-square.py](11-square.py)</pre><!--@schambig--> | Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).<br>• Instantiation with size: `def __init__(self, size):`<br>• the `area()` method must be implemented<br>• `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>` |
<!-- <pre><br><br></pre> • <br>• -->`

##  Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-inheritance
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
