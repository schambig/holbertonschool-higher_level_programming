<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# JavaScript Objects, Scopes and Closures<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

JavaScript (or "JS") is a programming language used most often for dynamic client-side scripts on webpages, but it is also often used on the server-side, using a runtime such as Node.js.

JavaScript is primarily used in the browser, enabling developers to manipulate webpage content through the DOM, manipulate data with AJAX and IndexedDB, draw graphics with canvas, interact with the device running the browser through various APIs, and more.

In this project we will work with objects, scopes and closures.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* How to create an object in JavaScript
* What `this` means
* What `undefined` means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## Resources<!--@schambig-->

Important concepts to help you understand this project:

* [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript) (read all examples!)
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
* [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
* [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* This code is `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-rectangle.js](0-rectangle.js)</pre><!--@schambig--> | Write an empty class `Rectangle` that defines a rectangle:<br>• You must use the `class` notation for defining your class |
| <pre>[1-rectangle.js](1-rectangle.js)</pre><!--@schambig--> | Write a class `Rectangle` that defines a rectangle:<br>• You must use the `class` notation for defining your class<br>• The constructor must take 2 arguments `w` and `h`<br>• Initialize the instance attribute `width` with the value of `w`<br>• Initialize the instance attribute `height` with the value of `h` |
| <pre>[2-rectangle.js](2-rectangle.js)</pre><!--@schambig--> | Write a class `Rectangle` that defines a rectangle:<br>• You must use the `class` notation for defining your class<br>• The constructor must take 2 arguments `w` and `h`<br>• Initialize the instance attribute `width` with the value of `w`<br>• Initialize the instance attribute `height` with the value of `h`<br>• If `w` or `h` is equal to 0 or not a positive integer, create an empty object |
| <pre>[3-rectangle.js](3-rectangle.js)</pre><!--@schambig--> | Write a class `Rectangle` that defines a rectangle:<br>• You must use the `class` notation for defining your class<br>• The constructor must take 2 arguments `w` and `h`<br>• Initialize the instance attribute `width` with the value of `w`<br>• Initialize the instance attribute `height` with the value of `h`<br>• If `w` or `h` is equal to 0 or not a positive integer, create an empty object<br>• Create an instance method called `print()` that prints the rectangle using the character `X` |
| <pre>[4-rectangle.js](4-rectangle.js)</pre><!--@schambig--> | Write a class `Rectangle` that defines a rectangle:<br>• You must use the `class` notation for defining your class<br>• The constructor must take 2 arguments `w` and `h`<br>• Initialize the instance attribute `width` with the value of `w`<br>• Initialize the instance attribute `height` with the value of `h`<br>• If `w` or `h` is equal to 0 or not a positive integer, create an empty object<br>• Create an instance method called `print()` that prints the rectangle using the character `X`<br>• Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle<br>• Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2 |
| <pre>[5-square.js](5-square.js)</pre><!--@schambig--> | Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:<br>• You must use the `class` notation for defining your class and `extends`<br>• The constructor must take 1 argument: `size`<br>• The constructor of `Rectangle` must be called (by using `super()`) |
| <pre>[6-square.js](6-square.js)</pre><!--@schambig--> | Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:<br>• You must use the `class` notation for defining your class and `extends`<br>• Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`<br>&nbsp;&nbsp;&nbsp;&nbsp;• If `c` is `undefined`, use the character `X` |
| <pre>[7-occurrences.js](7-occurrences.js)</pre><!--@schambig--> |  |
| <pre>[8-esrever.js](8-esrever.js)</pre><!--@schambig--> |  |
| <pre>[9-logme.js](9-logme.js)</pre><!--@schambig--> |  |
| <pre>[10-converter.js](10-converter.js)</pre><!--@schambig--> |  |
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
