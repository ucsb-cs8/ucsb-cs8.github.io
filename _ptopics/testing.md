---
topic: Testing
desc: Various ways of testing Python functions
---

There are various strategies for testing Python functions.   Each of these is appropriate at a certain stage in your development 
as a Python programmer.

# Simple Interactive Testing in IDLE

If you are just getting started with Python, you might be using IDLE as the program through which you interact with Python.
IDLE is an "Integrated Development Environment (IDE)" for Python&mdash;that is, a tool in which you can create Python programs,
make changes to them, save them, and run them to see what they do.

In IDLE, to test a function, you can use the "File->New Window" command to open up a new file in 
which to write a function such as this one:

```
def area_rect(length,width):
   return length * width
```

You can then execute the file by selecting "Run -> Run Module". This will prompt you to save the file; you should give it a name
such as `area.py` and then save it. 

Then you'll see that *in a separate window*, the so-called `Python Shell` window, that the file has been loaded.  That looks like this:

```
Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> 
```

At the `>>> ` prompt, you can type *function calls* to the `area_rect` function to test it. That looks like this:

```
>>> area_rect(10,5)
50
>>> area_rect(2.5,2)
5.0
>>> 
```

You can see that for each function call, the Python Shell (also known as the Python REPL, for "Read Eval Print Loop") reads your function call, evaluates it, prints the answer, and then loops back to show you another `>>> ` prompt.

This way of testing is appropriate when you are first starting with Python.  But it is tedious.  You have to type in the test cases every single time you make a change to a function, and you can only run one test at a time.  So as you make progress as a programmer, you'll likely want to move on to more powerful ways of testing your code.

# Better ways of testing

A few better ways of testing include:

* [pytest](/topics/pytest)
* [unittest](/topics/unittest)
