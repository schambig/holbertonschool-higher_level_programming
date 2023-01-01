<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# Python hello-world<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language, it has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

This project is about working with modules which are files containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

## Resources<!--@schambig-->

Important concepts for this project:

* [Modules](https://docs.python.org/3/tutorial/modules.html)
* [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-add.py](0-add.py)</pre><!--@schambig--> | Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`<br>• You have to use `print` function with string format to display integers<br>• You have to assign:<br>&nbsp;&nbsp;&nbsp;&nbsp;- the value `1` to a variable called `a`<br>&nbsp;&nbsp;&nbsp;&nbsp;- the value `2` to a variable called `b`<br>&nbsp;&nbsp;&nbsp;&nbsp;- and use those two variables as arguments when calling the functions `add` and `print`<br>• `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`<br>• Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line<br>• You can only use the word `add_0` once in your code<br>• You are not allowed to use `*` for importing or `__import__`<br>• Your code should not be executed when imported - by using `__import__`, like the example below |
| <pre>[1-calculation.py](1-calculation.py)</pre><!--@schambig--> | Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result<br>• Do not use the function `print` more than 4 times<br>• You have to define:<br>&nbsp;&nbsp;&nbsp;&nbsp;- the value `10` to a variable `a`<br>&nbsp;&nbsp;&nbsp;&nbsp;- the value `5` to a variable `b`<br>&nbsp;&nbsp;&nbsp;&nbsp;- and use those two variables only, as arguments when calling functions (including `print`)<br>• `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`<br>• Your program should call each of the imported functions. See example below for format<br>• the word `calculator_1` should be used only once in your file<br>• You are not allowed to use `*` for importing or `__import__`<br>• Your code should not be executed when imported |
| <pre>[2-args.py](2-args.py)</pre><!--@schambig--> | Write a program that prints the number of and the list of its arguments given from CLI<br>• The output should be:<br>&nbsp;&nbsp;&nbsp;&nbsp;- Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by<br>&nbsp;&nbsp;&nbsp;&nbsp;- `:` (or `.` if no arguments were passed) followed by <br>&nbsp;&nbsp;&nbsp;&nbsp;- a new line, followed by (if at least one argument),<br>&nbsp;&nbsp;&nbsp;&nbsp;- one line per argument:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line<br>• Your code should not be executed when imported<br>• he number of elements of `argv` can be retrieved by using: `len(argv)`<br>• You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them |
| <pre>[3-infinite_add.py](3-infinite_add.py)</pre><!--@schambig--> | Write a program that prints the result of the addition of all arguments from CLI<br>• The output should be the result of the addition of all arguments, followed by a new line<br>• You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)<br>• Your code should not be executed when imported |
| <pre>[4-hidden_discovery.py](4-hidden_discovery.py)</pre><!--@schambig--> | Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc)<br>• You should print one name per line, in alpha order<br>• You should print only names that do not start with `__`<br>• Your code should not be executed when imported<br>• Make sure you are running your code in Python3.8.x (`hidden_4.pyc` has been compiled with this version) |
| <pre>[5-variable_load.py](5-variable_load.py)</pre><!--@schambig--> | Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value<br>• You are not allowed to use `*` for importing or `__import__`<br>• Your code should not be executed when imported |
| <pre>[100-my_calculator.py](100-my_calculator.py)</pre><!--@schambig--> | Write a program that imports all functions from the file `calculator_1.py` and handles basic operations. |
| <pre>[102-magic_calculation.py](102-magic_calculation.pyy)</pre><!--@schambig--> |  |
<!-- <pre><br><br></pre> • <br>•-->


## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-import_modules
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
