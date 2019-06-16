---
topic: Testing
desc: Various ways of testing Python functions
---

There are various strategies for testing Python functions.   Each of these is appropriate at a certain stage in your development 
as a Python programmer.

# Simple Testing in IDLE

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

