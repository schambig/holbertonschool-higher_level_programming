<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# Python Input/Output<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language, it has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

In this project we will use `open()` function with its modes `w`: write, `r`: read, also we will work with the `json` module to serialize and deserialize objects.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the `with` statement
* What is `JSON`
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

## Resources<!--@schambig-->

Important concepts to help you understand this project:

* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (until “11.4 Binary Files” (included))
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU) (Derek Banas video)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (ch. 8 p 180-183 and ch. 14 p 326-333)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these source code use the pycodestyle (version 2.7.*)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-read_file.py](0-read_file.py)</pre><!--@schambig--> | Write a function that reads a text file (` UTF8`) and prints it to stdout:<br>• Prototype: `def read_file(filename=""):`<br>• You must use the `with` statement<br>• You don’t need to manage `file permission` or `file doesn't exist` exceptions.<br>• You are not allowed to import any module |
| <pre>[1-write_file.py](1-write_file.py)</pre><!--@schambig--> | Write a function that writes a string to a text file (UTF8) and returns the number of characters written: |
| <pre>[2-append_write.py](2-append_write.py)</pre><!--@schambig--> | Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added: |
| <pre>[3-to_json_string.py](3-to_json_string.py)</pre><!--@schambig--> |  |
| <pre>[4-from_json_string.py](4-from_json_string.py)</pre><!--@schambig--> |  |
| <pre>[5-save_to_json_file.py](5-save_to_json_file.py)</pre><!--@schambig--> |  | 
| <pre>[6-load_from_json_file.py](6-load_from_json_file.py)</pre><!--@schambig--> |  |
| <pre>[7-add_item.py](7-add_item.py)</pre><!--@schambig--> |  |
| <pre>[8-class_to_json.py](8-class_to_json.py)</pre><!--@schambig--> |  |
| <pre>[9-student.py](9-student.py)</pre><!--@schambig--> |  |
| <pre>[10-student.py](10-student.py)</pre><!--@schambig--> |  |
| <pre>[11-student.py](11-student.py)</pre><!--@schambig--> |  |
| <pre>[12-pascal_triangle.py](12-pascal_triangle.py)</pre><!--@schambig--> |  |
<!-- <pre><br><br></pre> • <br>•-->

## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd python-input_output
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
