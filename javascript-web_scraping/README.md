<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)<!--@schambig-->
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/holbertonschool-higher_level_programming)<!--@schambig-->
[![C|C](https://img.shields.io/badge/Repo-00%20commits-orange.svg)](https://sourcerer.io/schambig)<!--@schambig-->

# JavaScript Web Scraping<!--@schambig-->

[Description](#description) • [Resources](#resources) • <!--@schambig-->[File Structure](#file-structure) • [Usage](#usage)

---

## Description<!--@schambig-->

JavaScript (or "JS") is a programming language used most often for dynamic client-side scripts on webpages, but it is also often used on the server-side, using a runtime such as Node.js.

JavaScript is primarily used in the browser, enabling developers to manipulate webpage content through the DOM, manipulate data with AJAX and IndexedDB, draw graphics with canvas, interact with the device running the browser through various APIs, and more.

In this project we are going to use `fs` and `request` modules to make requests from an API.

After this project I was able to [explain to anyone](https://fs.blog/feynman-learning-technique/):

* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module


## Resources<!--@schambig-->

Important concepts to help you understand this project:

* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
* [request module](https://github.com/request/request)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code.

* All these files were interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* This code is `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)

| Filename | Description/Task |
| --- | --- |
| <pre>[0-readme.js](0-readme.js)</pre><!--@schambig--> | Write a script that reads and prints the content of a file.<br>• The first argument is the file path<br>• The content of the file must be read in `utf-8`<br>• If an error occurred during the reading, print the error object |
| <pre>[1-writeme.js](1-writeme.js)</pre><!--@schambig--> | Write a script that writes a string to a file.<br>• The first argument is the file path<br>• The second argument is the string to write<br>• The content of the file must be read in `utf-8`<br>• If an error occurred during while writing, print the error object |
| <pre>[2-statuscode.js](2-statuscode.js)</pre><!--@schambig--> | Write a script that display the status code of a `GET` request.<br>• The first argument is the URL to request (`GET`)<br>• The status code must be printed like this: code: `<status code>`<br>• You must use the module `request` |
| <pre>[3-starwars_title.js](3-starwars_title.js)</pre><!--@schambig--> | Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.<br>• The first argument is the movie ID<br>• You must use the [`Star wars API`](https://swapi-api.hbtn.io/) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`<br>• You must use the module `request` |
| <pre>[4-starwars_count.js](4-starwars_count.js)</pre><!--@schambig--> | Write a script that prints the number of movies where the character “Wedge Antilles” is present.<br>• he first argument is the API URL of the [`Star wars API`](https://swapi-api.hbtn.io/): `https://swapi-api.hbtn.io/api/films/`<br>• Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API<br>• You must use the module `request` |
| <pre>[5-request_store.js](5-request_store.js)</pre><!--@schambig--> | Write a script that gets the contents of a webpage and stores it in a file.<br>• The first argument is the URL to request<br>• The second argument the file path to store the body response<br>• The file must be UTF-8 encoded<br>• You must use the module `request` |
| <pre>[6-completed_tasks.js](6-completed_tasks.js)</pre><!--@schambig--> | Write a script that computes the number of tasks completed by user id.<br>• The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`<br>• Only print users with completed task<br>• You must use the module `request` |
<!-- <pre><br><br></pre> • <br>•-->

## Usage<!--@schambig-->

To try this project, first clone the repository to your machine :

```
$ git clone https://github.com/schambig/holbertonschool-higher_level_programming.git
```

Then, go to the project directory:

```
$ cd javascript-web_scraping
```

Finally, you can execute the scripts:

```
$ ./[FILENAME]
```


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
