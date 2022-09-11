<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)
[![C|C](https://img.shields.io/badge/Repo-35%20commits-orange.svg)](https://sourcerer.io/schambig)

# Python hello-world<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[Zen of Python](#zen-of-python) • [File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991. It is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

This project covers the basics of Pyhton.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the [Zen of Python](#zen-of-python)
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with `pycodestyle`

## Resources<!--@schambig-->

Important concepts for this project:

* [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters)
* [The Python Guru](https://thepythonguru.com/)
* [Python string formatting](https://pyformat.info)
* [Garbage collector](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)
* [Python Interpreter](http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
* [Python bytecode](https://docs.python.org/3.4/library/dis.html)

More valuable resources to help you understand this project:

* [Python Programming: An Introduction to Computer Science 3rd edition](https://www.pdfdrive.com/python-programming-an-introduction-to-computer-science-e183602644.html)
* [Derek Banas’ Learn to program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
* `Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

## Zen of Python<!--@schambig-->

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-run](0-run)</pre><!--@schambig--> | Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE` |
| <pre>[1-run_inline](1-run_inline)</pre><!--@schambig--> | Write a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE` |
| <pre>[2-print.py](2-print.py)</pre><!--@schambig--> | Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line. Use the function print |
| <pre>[3-print_number.py](3-print_number.py)</pre><!--@schambig--> | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line. You are not allowed to cast the variable number into a string, Your code must be 3 lines long, You have to use f-strings [tips](https://realpython.com/python-f-strings/) |
| <pre>[4-print_float.py](4-print_float.py)</pre><!--@schambig--> | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits. You are not allowed to cast number to string, You have to use f-strings. |
| <pre>[5-print_string.py](5-print_string.py)</pre><!--@schambig--> | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters. You are not allowed to use any loops or conditional statement, Your program should be maximum 5 lines long. |
| <pre>[6-concat.py](6-concat.py)</pre><!--@schambig--> | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`. You are not allowed to use any loops or conditional statements, You have to use the variables `str1` and `str2` in your new line of code, Your program should be exactly 5 lines long. |
| <pre>[7-edges.py](7-edges.py)</pre><!--@schambig--> | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py), `word_first_3` should contain the first 3 letters of the variable `word`, `word_last_2` should contain the last 2 letters of the variable `word`, `middle_word` should contain the value of the variable `word` without the first and last letters. |
| <pre>[8-concat_edges.py](8-concat_edges.py)</pre><!--@schambig--> | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line. You are not allowed to use any loops or conditional statements, Your program should be exactly 5 lines long, You are not allowed to create new variables, You are not allowed to use string literals. |
| <pre>[9-easter_egg.py](9-easter_egg.py)</pre><!--@schambig--> | Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line. |
| <pre>[100-write.py](100-write.py)</pre><!--@schambig--><!--@schambig--> | Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line. Use the function `write` from the `sys` module, You are not allowed to use `print`, Your script should print to `stderr`, our script should exit with the status code `1`. |
| <pre>[101-compile](101-compile)</pre><!--@schambig--> | Write a Shell script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`, The output filename has to be `$PYFILEc` |
| <pre>[102-magic_calculation.py](102-magic_calculation.py)</pre><!--@schambig--> | Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode: <pre>  3           0 LOAD_CONST               1 (98)<br>              3 LOAD_FAST                0 (a)<br>              6 LOAD_FAST                1 (b)<br>              9 BINARY_POWER<br>             10 BINARY_ADD<br>             11 RETURN_VALUE</pre>  Tip: [Python bytecode](https://docs.python.org/3/library/dis.html). |

## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-hello_world
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
