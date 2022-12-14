<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# Python Data Structures<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language, it has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

This project covers `List` and `Tuples` data structures in Python and how to use Lists as `Stacks` and `Queues`.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it

## Resources<!--@schambig-->

Important concepts for this project:

* [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until 5.3. Tuples and Sequences included)
* [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-print_list_integer.py](0-print_list_integer.py)</pre><!--@schambig--> | Write a function that prints all integers of a list.<br>• Prototype: `def print_list_integer(my_list=[]):`<br>• Format: one integer per line<br>• You are not allowed to import any module<br>• You can assume that the list only contains integers<br>• You are not allowed to cast integers into strings<br>• You have to use `str.format()` to print integers |
| <pre>[1-element_at.py](1-element_at.py)</pre><!--@schambig--> | Write a function that retrieves an element from a list like in C.<br>• Prototype: `def element_at(my_list, idx):`<br>• If `idx` is negative, the function should return `None`<br>• If `idx` is out of range (> of number of element in `my_list`), the function should return `None`<br>• You are not allowed to import any module<br>• You are not allowed to use `try/except` |
| <pre>[2-replace_in_list.py](2-replace_in_list.py)</pre><!--@schambig--> | Write a function that replaces an element of a list at a specific position (like in C).<br>• Prototype: `def replace_in_list(my_list, idx, element):`<br>• If `idx` is negative, the function should not modify anything, and returns the original list<br>• If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list<br>• You are not allowed to import any module<br>• You are not allowed to use `try/except` |
| <pre>[3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)</pre><!--@schambig--> | Write a function that prints all integers of a list, in reverse order.<br>• Prototype: `def print_reversed_list_integer(my_list=[]):`<br>• Format: one integer per line<br>• You are not allowed to import any module<br>• You can assume that the list only contains integers<br>• You are not allowed to cast integers into strings<br>• You have to use `str.format()` to print integers |
| <pre>[4-new_in_list.py](4-new_in_list.py)</pre><!--@schambig--> | Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).<br>• Prototype: `def new_in_list(my_list, idx, element):`<br>• If `idx` is negative, the function should return a copy of the original `list`<br>• If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`<br>• You are not allowed to import any module<br>• You are not allowed to use `try/except` |
| <pre>[5-no_c.py](5-no_c.py)</pre><!--@schambig--> | Write a function that removes all characters `c` and `C` from a string.<br>• Prototype: `def no_c(my_string):`<br>• The function should return the new string<br>• You are not allowed to import any module<br>• You are not allowed to use `str.replace()` |
| <pre>[6-print_matrix_integer.py](6-print_matrix_integer.py)</pre><!--@schambig--> | Write a function that prints a matrix of integers.<br>• Prototype: `def print_matrix_integer(matrix=[[]]):`<br>• You are not allowed to import any module<br>• You can assume that the list only contains integers<br>• You are not allowed to cast integers into strings<br>• You have to usThe new list should have the same size as the original liste `str.format()` to print integers |
| <pre>[7-add_tuple.py](7-add_tuple.py)</pre><!--@schambig--> | Write a function that adds 2 tuples.<br>• Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`<br>• Returns a tuple with 2 integers:<br>&nbsp;&nbsp;&nbsp;&nbsp;- The first element should be the addition of the first element of each argument<br>&nbsp;&nbsp;&nbsp;&nbsp;- The second element should be the addition of the second element of each argument<br>• You are not allowed to import any module<br>• You can assume that the two tuples will only contain integers<br>• If a tuple is smaller than 2, use the value `0` for each missing integer<br>• If a tuple is bigger than 2, use only the first 2 integers |
| <pre>[8-multiple_returns.py](8-multiple_returns.py)</pre><!--@schambig--> | Write a function that returns a tuple with the length of a string and its first character.<br>• Prototype: `def multiple_returns(sentence):`<br>• If the sentence is empty, the first character should be equal to `None`<br>• You are not allowed to import any module |
| <pre>[9-max_integer.py](9-max_integer.py)</pre><!--@schambig--> | Write a function that finds the biggest integer of a list.<br>• Prototype: `def max_integer(my_list=[]):`<br>• If the list is empty, return `None`<br>• You can assume that the list only contains integers<br>• You are not allowed to import any module<br>• You are not allowed to use the builtin `max()` |
| <pre>[10-divisible_by_2.py](10-divisible_by_2.py)</pre><!--@schambig--> | Write a function that finds all multiples of 2 in a list.<br>• Prototype: `def divisible_by_2(my_list=[]):`<br>• Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2<br>• The new list should have the same size as the original list<br>• You are not allowed to import any module |
| <pre>[11-delete_at.py](11-delete_at.py)</pre><!--@schambig--> | Write a function that deletes the item at a specific position in a list.<br>• Prototype: `def delete_at(my_list=[], idx=0):`<br>• If `idx` is negative or out of range, nothing change (returns the same list)<br>• You are not allowed to use `pop()`<br>• You are not allowed to import any module |
| <pre>[12-switch.py](12-switch.py)</pre><!--@schambig--> | Complete [this source code](https://github.com/hs-hq/0x03.py/blob/main/12-switch_py) in order to switch value of `a` and `b`.<br>• Your code should be inserted where the comment is (line 4)<br>• Your program should be exactly 5 lines long |
<!-- <pre><br><br></pre> • <br>•-->


## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-data_structures
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
