<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# Python Everything is an Object<!--@schambig-->

[Background Context](#background-context) • [Description](#description) • [Medium Blogpost](#medium-blogpost) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Background Context<!--@schambig-->

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
```

OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```

## Description<!--@schambig-->

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. 

All answers will be only one line in a file. No space before or after the answer.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions


## Medium Blogpost<!--@schambig-->

After finishing this project I've written a blogpost about everything I learned and I would like you to read it. [Click here](https://medium.com/@schambig/python3-mutable-and-immutable-objects-c7c70bfb067a)

![Medium Blogpost](https://i.imgur.com/ZGpeodW.jpg)

## Resources<!--@schambig-->

Important concepts to help you understand this project:

* [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
* [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
* [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
* [Mutation](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects) (Only this chapter)
* [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
* [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-answer.txt](0-answer.txt)</pre><!--@schambig--> | What function would you use to print the type of an object?<br>Write the name of the function in the file, without `()`. |
| <pre>[1-answer.txt](1-answer.txt)</pre><!--@schambig--> | How do you get the variable identifier (which is the memory address in the CPython implementation)?<br>Write the name of the function in the file, without `()`. |
| <pre>[2-answer.txt](2-answer.txt)</pre><!--@schambig--> | In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`. <pre>>>> a = 89<br>>>> b = 100</pre> |
| <pre>[3-answer.txt](3-answer.txt)</pre><!--@schambig--> | In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`. <pre>>>> a = 89<br>>>> b = 89</pre> |
| <pre>[4-answer.txt](4-answer.txt)</pre><!--@schambig--> | In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`. <pre>>>> a = 89<br>>>> b = a</pre> |
| <pre>[5-answer.txt](5-answer.txt)</pre><!--@schambig--> | In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`. <pre>>>> a = 89<br>>>> b = a + 1</pre> |
| <pre>[6-answer.txt](6-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> s1 = "Best School"<br>>>> s2 = s1<br>>>> print(s1 == s2)</pre> |
| <pre>[7-answer.txt](7-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> s1 = "Best"<br>>>> s2 = s1<br>>>> print(s1 is s2)</pre> |
| <pre>[8-answer.txt](8-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> s1 = "Best School"<br>>>> s2 = "Best School"<br>>>> print(s1 == s2)</pre> |
| <pre>[9-answer.txt](9-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> s1 = "Best School"<br>>>> s2 = "Best School"<br>>>> print(s1 is s2)</pre> |
| <pre>[10-answer.txt](10-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> l1 = [1, 2, 3]<br>>>> l2 = [1, 2, 3]<br>>>> print(l1 == l2)</pre> |
| <pre>[11-answer.txt](11-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> l1 = [1, 2, 3]<br>>>> l2 = [1, 2, 3]<br>>>> print(l1 is l2)</pre> |
| <pre>[12-answer.txt](12-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> l1 = [1, 2, 3]<br>>>> l2 = l1<br>>>> print(l1 == l2)</pre> |
| <pre>[13-answer.txt](13-answer.txt)</pre><!--@schambig--> | What do these 3 lines print? <pre>>>> l1 = [1, 2, 3]<br>>>> l2 = l1<br>>>> print(l1 is l2)</pre> |
| <pre>[14-answer.txt](14-answer.txt)</pre><!--@schambig--> | What does this script print? <pre>l1 = [1, 2, 3]<br>l2 = l1<br>l1.append(4)<br>print(l2)</pre> |
| <pre>[15-answer.txt](15-answer.txt)</pre><!--@schambig--> | What does this script print? <pre>l1 = [1, 2, 3]<br>l2 = l1<br>l1 = l1 + [4]<br>print(l2)</pre> |
| <pre>[16-answer.txt](16-answer.txt)</pre><!--@schambig--> | What does this script print? <pre>def increment(n):<br>    n += 1<br><br>a = 1<br>increment(a)<br>print(a)</pre> |
| <pre>[17-answer.txt](17-answer.txt)</pre><!--@schambig--> | What does this script print? <pre>def increment(n):<br>    n.append(4)<br><br>l = [1, 2, 3]<br>increment(l)<br>print(l)</pre> |
| <pre>[18-answer.txt](18-answer.txt)</pre><!--@schambig--> | What does this script print? <pre>def assign_value(n, v):<br>    n = v<br><br>l = [1, 2, 3]<br>l2 = [4, 5, 6]<br>assign_value(l1, l2)<br>print(l1)</pre> |
| <pre>[19-copy_list.py](19-copy_list.py)</pre><!--@schambig--> | Write a function `def copy_list(l):` that returns a copy of a list.<br>• The input list can contain any type of objects<br>• Your file should be maximum 3-line long (no documentation needed)<br>• You are not allowed to import any module |
| <pre>[20-answer.txt](20-answer.txt)</pre><!--@schambig--> | Is `a` a tuple? Answer with `Yes` or `No`. <pre>a = ()</pre> |
| <pre>[21-answer.txt](21-answer.txt)</pre><!--@schambig--> | Is `a` a tuple? Answer with `Yes` or `No`. <pre>a = (1, 2)</pre> |
| <pre>[22-answer.txt](22-answer.txt)</pre><!--@schambig--> | Is `a` a tuple? Answer with `Yes` or `No`. <pre>a = (1)</pre> |
| <pre>[23-answer.txt](23-answer.txt)</pre><!--@schambig--> | Is `a` a tuple? Answer with `Yes` or `No`. <pre>a = (1, )</pre> |
| <pre>[24-answer.txt](24-answer.txt)</pre><!--@schambig--> | What does this script print? <pre>a = (1)<br>b = (1)<br>a is b</pre> |
| <pre>[25-answer.txt](25-answer.txt)</pre><!--@schambig--> |  |
| <pre>[26-answer.txt](26-answer.txt)</pre><!--@schambig--> |  |
| <pre>[27-answer.txt](27-answer.txt)</pre><!--@schambig--> |  |
| <pre>[28-answer.txt](28-answer.txt)</pre><!--@schambig--> |  |
<!-- <pre><br><br></pre> • -->

## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-everything_is_object
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
