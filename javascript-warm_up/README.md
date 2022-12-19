<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# JavaScript Warm Up<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

JavaScript (or "JS") is a programming language used most often for dynamic client-side scripts on webpages, but it is also often used on the server-side, using a runtime such as Node.js.

JavaScript is primarily used in the browser, enabling developers to manipulate webpage content through the DOM, manipulate data with AJAX and IndexedDB, draw graphics with canvas, interact with the device running the browser through various APIs, and more.

In this project we will learn the basic concepts of the language and do some scripting .

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between `var`, `const` and `let`
* What are all the data types available in JavaScript
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use `while` and `for` loops
* How to use `break` and `continue` statements
* What is a function and how do you use functions
* What does a function that does not use any `return` statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

## Resources<!--@schambig-->

Important concepts to help you understand this project:

* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://intranet.hbtn.io/rltoken/tEH_XriewD7BUQux0ADN0w)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)
* [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8) (`Fun Fun Function` video)
* [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI) (`LearnCode.academy` video)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* This code is `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-javascript_is_amazing.js](0-javascript_is_amazing.js)</pre><!--@schambig--> | Write a script that prints “JavaScript is amazing”:<br>• You must create a constant variable called `myVar` with the value “JavaScript is amazing”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var` |
| <pre>[1-multi_languages.js](1-multi_languages.js)</pre><!--@schambig--> | Write a script that prints 3 lines:<br>• The first line: “C is fun”<br>• The second line: “Python is cool”<br>• The third line: “JavaScript is amazing”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var` |
| <pre>[2-arguments.js](2-arguments.js)</pre><!--@schambig--> | Write a script that prints a message depending of the number of arguments passed:<br>• If no arguments are passed to the script, print “No argument”<br>• If only one argument is passed to the script, print “Argument found”<br>• Otherwise, print “Arguments found”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var`<br>Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv) |
| <pre>[3-value_argument.js](3-value_argument.js)</pre><!--@schambig--> | Write a script that prints the first argument passed to it:<br>• If no arguments are passed to the script, print “No argument”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var`<br>• You are not allowed to use `length` |
| <pre>[4-concat.js](4-concat.js)</pre><!--@schambig--> | Write a script that prints two arguments passed to it, in the following format: “ is ”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var` |
| <pre>[5-to_integer.js](5-to_integer.js)</pre><!--@schambig--> | Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:<br>• If the argument can’t be converted to an integer, print “Not a number”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var`<br>• You are not allowed to use `try/catch` |
| <pre>[6-multi_languages_loop.js](6-multi_languages_loop.js)</pre><!--@schambig--> | Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop<br>• The first line: “C is fun”<br>• The second line: “Python is cool”<br>• The third line: “JavaScript is amazing”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var`<br>• You are not allowed to use any `if/else` statement<br>• You can use only one `console.log`<br>• You must use a loop (`while`, `for`, etc.) |
| <pre>[7-multi_c.js](7-multi_c.js)</pre><!--@schambig--> | Write a script that prints `x` times “C is fun”<br>• Where `x` is the first argument of the script<br>• If the first argument can’t be converted to an integer, print “Missing number of occurrences”<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var`<br>• You can use only two `console.log`<br>• You must use a loop (`while`, `for`, etc.) |
| <pre>[8-square.js](8-square.js)</pre><!--@schambig--> | Write a script that prints a square<br>• The first argument is the size of the square<br>• If the first argument can’t be converted to an integer, print “Missing size”<br>• You must use the character `X` to print the square<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var`<br>• You must use a loop (`while`, `for`, etc.) |
| <pre>[9-add.js](9-add.js)</pre><!--@schambig--> | Write a script that prints the addition of 2 integers<br>• The first argument is the first integer<br>• The second argument is the second integer<br>• You have to define a function with this prototype: `function add(a, b)`<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var` |
| <pre>[10-factorial.js](10-factorial.js)</pre><!--@schambig--> | Write a script that computes and prints a factorial<br>• The first argument is integer (argument can be cast as integer) used for computing the factorial<br>• Factorial of `NaN` is `1`<br>• You must do it recursively<br>• You must use a function<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var` |
| <pre>[11-second_biggest.js](11-second_biggest.js)</pre><!--@schambig--> | Write a script that searches the second biggest integer in the list of arguments.<br>• You can assume all arguments can be converted to integer<br>• If no argument passed, print `0`<br>• If the number of arguments is 1, print `0`<br>• You must use `console.log(...)` to print all output<br>• You are not allowed to use `var` |
| <pre>[12-object.js](12-object.js)</pre><!--@schambig--> | Update this script to replace the value `12` with `89`:<br>• You are not allowed to use `var` |
| <pre>[13-add.js](13-add.js)</pre><!--@schambig--> | Write a function that returns the addition of 2 integers.<br>• The function must be visible from outside<br>• The name of the function must be `add`<br>• You are not allowed to use `var` |
<!-- <pre><br><br></pre> • <br>•-->

## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd 
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
