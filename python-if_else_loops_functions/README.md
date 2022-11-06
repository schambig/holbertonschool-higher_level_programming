<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-37%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# Python if-else loops and functions<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991. It is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

This project ... .

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* Why indentation is so important in Python
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use the `while` and `for` loops
* How is Python’s `for` different from `C`‘s?
* How to use the `break` and `continues` statements
* How to use `else` clauses on loops
* What does the `pass` statement do, and when to use it
* How to use `range`
* What is a function and how do you use functions
* What does return a function that does not use any `return` statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them

## Resources<!--@schambig-->

Important concepts to help you undestand this project:

* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
* [Indentation in Python](https://www.programiz.com/python-programming/statement-indentation-comments)
* [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
* [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Learn to Program 2 : Looping](https://www.youtube.com/watch?v=swQEbZ6ez1I&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=2)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

Also don't forget to check the man pages:

* man python3


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-positive_or_negative.py](0-positive_or_negative.py)</pre><!--@schambig--> | This program will assign a random signed number to the variable `number` each time it is executed. Complete this [source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py) in order to print whether the number stored in the variable `number` is positive or negative. |
| <pre>[1-last_digit.py](1-last_digit.py)</pre><!--@schambig--> | This program will assign a random signed number to the variable `number` each time it is executed. Complete this [source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py) in order to print the last digit of the number stored in the variable `number`. |
| <pre>[2-print_alphabet.py](2-print_alphabet.py)</pre><!--@schambig--> | Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line. You can only use one `print` function with string format, only use one loop in your code, not allowed to store characters in a variable, not allowed to import any module. |
| <pre>[3-print_alphabt.py](3-print_alphabt.py)</pre><!--@schambig--> | Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line, print all the letters except `q` and `e`, only use one `print` function with string format, only use one loop in your code. |
| <pre>[4-print_hexa.py](4-print_hexa.py)</pre><!--@schambig--> | Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal, only use one print function with string format, only use one loop in your code. |
| <pre>[5-print_comb2.py](5-print_comb2.py)</pre><!--@schambig--> | Write a program that prints numbers from `0` to `99`, in ascending order, with two digits, only use no more than 2 `print` functions with string format, only use one loop in your code, in ascending order. |
| <pre>[6-print_comb3.py](6-print_comb3.py)</pre><!--@schambig--> | Write a program that prints all possible different combinations of two digits, separated by ,, followed by a space, `01` and `10` are considered the same combination of the two digits `0` and `1`, only use no more than 3 `print` functions with string format. |
| <pre>[7-islower.py](7-islower.py)</pre><!--@schambig--> | Write a function that checks for lowercase character. |
| <pre>[8-uppercase.py](8-uppercase.py)</pre><!--@s, chambig--> | Write a function that prints a string in uppercase followed by a new line. |
| <pre>[9-print_last_digit.py](9-print_last_digit.py)</pre><!--@schambig--> | Write a function that prints the last digit of a number. |
| <pre>[10-add.py](10-add.py)</pre><!--@schambig--> | Write a function that adds two integers and returns the result. |
| <pre>[11-pow.py](11-pow.py)</pre><!--@schambig--> | Write a function that computes `a` to the power of `b` and return the value. |
| <pre>[12-fizzbuzz.py](12-fizzbuzz.py)</pre><!--@schambig--> | Write a function that prints the numbers from 1 to 100 separated by a space, for multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`, for numbers which are multiples of both three and five print `FizzBuzz`, each element should be followed by a space. |
| <pre>[100-print_tebahpla.py](100-print_tebahpla.py)</pre><!--@schambig--> | Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line. |
| <pre>[101-remove_char_at.py](101-remove_char_at.py)</pre><!--@schambig--> | Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”). |
| <pre>[102-magic_calculation.py](102-magic_calculation.py)</pre><!--@schambig--> | Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode: <pre>  3           0 LOAD_FAST               0 (a)<br>              3 LOAD_FAST               1 (b)<br>              6 COMPARE_OP              0 (<)<br>              9 POP_JUMP_IF_FALSE      16<br><br>  4           12 LOAD_FAST              2 (c)<br>              15 RETURN_VALUE               <br><br>  5       >>  16 LOAD_FAST              2 (c)<br>              19 LOAD_FAST              1 (b)<br>              22 COMPARE_OP             4 (>)<br>              25 POP_JUMP_IF_FALSE     36<br><br>  6           28 LOAD_FAST              0 (a)<br>              31 LOAD_FAST              1 (b)<br>              34 BINARY_ADD               <br>              35 RETURN_VALUE               <br><br>  7       >>  36 LOAD_FAST              0 (a)<br>              39 LOAD_FAST              1 (b)<br>              42 BINARY_MULTIPLY               <br>              43 LOAD_FAST              2 (c)<br>              46 BINARY_SUBTRACT               <br>              47 RETURN_VALUE               <br><br> Tip: [Python bytecode](https://docs.python.org/3/library/dis.html). |

## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-if_else_loops_functions
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
