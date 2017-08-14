---
topic: "MacOS"
desc: "Using Python on MacOS"
---

This page is about using Python DIRECTLY on your MacOS system.

If instead, you want information about accessing the ECI/CSIL systems at UCSB using your MacOS system, see this page: 
[CSIL via MacOS](/topics/csil_via_macos/)


# Short version:

* Type `python` or `python3` to bring up Python at a terminal window
* Be sure you know what version of Python the `python` and/or `python3` command brings up on your system.
* Be sure you also know the difference between [Python 2 and Python 3](python2vs3/)
* If you don't have Python 3.6.2 or higher on your Mac, download and install the latest version of Python for MacOS from here: <https://www.python.org/downloads/>
* To exit the Python prompt (`>>>`) type `quit()` or Control-D (works on both Python&nbsp;2 and Python&nbsp;3)
* If you have both Python&nbsp;2 and 3 on your machine, for Python&nbsp;3 use:
    * `idle3` instead of `idle`
    * `pip3` instead of `pip`


    
# Checking if Python is installed already

As a reminder, there are two major versions of Python: Python&nbsp;2, and Python&nbsp;3.  (Read [more about Python&nbsp;2 vs.&nbsp;3 here](python2vs3/).
Your Mac may come with Python&nbsp;2 installed&mdash;if so, you should install Python&nbsp;3 to work on the assignments in this course, and to 
match the material in the textbook.

To determine what version of Python is the default on your system, open a Terminal window (see how [here](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line))
and type 'python`'

It may look something like this.  You can see from the output below that on my machine, I have Python 2.7.11 currently installed as the 
default for the `python` command.

```
Phills-MacBook-Pro:~ pconrad$ python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

(To exit,  type `quit()` followed by "enter/return" or hold down "control" while typing `D` (CTRL-D).)

I might also have Python&nbsp;3 installed in parallel with Python&nbsp;2.  In that case, typing `python3` will 
bring up Python&nbsp;3 as shown here:

```
Phills-MacBook-Pro:~ pconrad$ python3
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
(Again,  type `quit()` followed by "enter/return" or hold down "control" while typing `D` (CTRL-D).)

You should also have commands `idle` and `pip` available.    The Python3 versions may be `idle3` and `pip3`.

If you don't, see installation instructions below.

# Installing Python for MacOS

If you don't have Python 3.6.2 or higher on your Mac, download and install the latest version of Python for MacOS from here: <https://www.python.org/downloads/>

Once you've installed it, you should have either `python`, `idle` and `pip` commands that work for Python 3.6.2 (or else `python3`, `idle3` and `pip3` commands.)
