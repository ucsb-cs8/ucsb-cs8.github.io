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

# Interactive Testing without IDLE

If you aren't able to use IDLE for some reason, or simply prefer to use a different editor to create and make changes to files of Python code, it is still possible to do interactive testing as the command line.

Use whatever program code editor you like (e.g. Atom, VSCode, Sublime Text) to create your Python code in a file ending in `.py`.  For example, put this code in a file called `area.py`:


```
def area_rect(length,width):
   return length * width
```

Then, to test it, at the Unix prompt on CSIL, type:

```
python3 -i area.py
```

If you are using your own computer, you might need to type either `python3` or just plain `python`, like this:

```
python -i area.py
```

This loads the file `area.py`, and the `-i` flag means "interactive"&mdash;that is, you'll be given a `>>> ` Python Shell prompt to interact with your Python code after it loads.  Here's what that looks like. In this case, `cgaucho $` is the command line prompt.  It may look different on your system, and isn't part of what you type:

```
cgaucho $ python3 -i area.py
>>> 
```

At the `>>> ` prompt, you can start typing Python function calls to test your code.  You can type `quit()` when you are finished.

```
>>> area_rect(3,7)
21
>>> area_rect(3.5,4)
14.0
>>> quit()
```


# Better ways of testing

This way of testing is appropriate when you are first starting with Python.  But it is tedious.  You have to type in the test cases every single time you make a change to a function, and you can only run one test at a time.  So as you make progress as a programmer, you'll likely want to move on to more powerful ways of testing your code.

A few better ways of testing include:

* [pytest](/ptopics/pytest)
* [unittest](/ptopics/unittest)
