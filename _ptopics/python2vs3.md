---
topic: "Python 2 vs. Python 3"
desc: "Understanding the difference and why it matters"
---

There are two major versions of Python in common use today: 

* Python 2, sometimes written Python 2.x.
* Python 3, sometimes written Python 3.x

The 2.x and 3.x stand for the fact that the "latest" version of both Python 2 and Python 3 keeps changing over time.

On August 7, 2017, the latest 2.x was 2.7.13, and the latest version of 3.x was 3.6.2, but by the time you read this, either or both of those
numbers may no longer be the latest versions.   You can find out what the latest version is by visiting 
<https://www.python.org/downloads/>.

# Why are there two different versions out there?

The creator of Python, Guido van Rossum, decided that some major changes to Python needed to be made in order to 
improve the language, when Python 3.0 was introduced.    But, those changes "broke" older systems that were still using
Python&nbsp;2.    And, many useful libraries that Python programs depended on were not available in Python 3.0 for a very long time.

As a result, Python&nbsp;2 and Python&nbsp;3, although *very* similar, are *just* different enough that they are really
different languages.      

* Code written for Python 2 may not run correctly, or at all, on Python 3 systems.
* Code written for Python 3 may not run correctly, or at all, on Python 2 systems.

One change that you see immediately relates to the `print` feature: in Python 2, it's a keyword built into the language, while in Python&nbsp;3, it is a 
function call.   This may seem like a minor change, but its enough to break many programs.   Another change is how the division operator
works.  And there are many more such changes.

# What version should I use

In this course, we've chosen to use Python 3.    By now, most of the major useful libraries *are* available for Python&nbsp;3, and that is the
future direction for the language.   

However, many computer systems may still have Python 2 installed as the "default" Python, that is, the one you get if you don't specify.

Be sure, therefore, that if you are using your own computer, that you install Python 3.x, and bring that up every time you work on Python code.

If you are using a system maintained by someone else, be sure that you know the proper commands to access Python 3 versions of software needed for the course.    

* On systems with both, the Python command line is usually accessed with `python3` instead of `python`
* IDLE is accessed with `idle3` instead of `idle`
* pip is accessed with `pip3` instead of `pip`

# Checking Python version

Type `python` and `python3` and see what version comes up, e.g.

```
-bash-4.3$ python
Python 2.7.11 (default, Sep 29 2016, 13:33:00) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
-bash-4.3$ python3
Python 3.4.3 (default, Aug  9 2016, 15:36:17) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
-bash-4.3$ 
```

# Checking IDLE version

When running `idle` or `idle3`, the version of Python it is built for shows up in the window that pops up, e.g.

```
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16) 
```

vs

```
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
```

# Checking pip version

To check the version of pip, use `pip -V` or `pip3 -V`

```
-bash-4.3$ pip -V
pip 7.1.0 from /usr/lib/python2.7/site-packages (python 2.7)
-bash-4.3$ pip3 -V
pip 7.1.0 from /usr/lib/python3.4/site-packages (python 3.4)
-bash-4.3$ 
```
