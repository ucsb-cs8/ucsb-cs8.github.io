---
topic: "files"
desc: "reading and writing files in Python"
---

# References

Here are several references 

# Opening and Closing Files

The simplest code to open an input file looks like this (see p. 109 in Perkovic 2nd edition)

```
infile = open('example.txt', 'r')
```

If you do it this way, you have the obligation to later close the file, like this, when you are finished with it:

```
infile.close()
```

A way that may Python programmers prefer is to use a `with` statement, like this:

```
  with open('example.txt','r') as infile:
     data = infile.read()
```

With this style of coding, all the code you want to do while the file is open is done inside the indented
`with` block.   The file `infile` is automatically closed as soon as the indented block is exited.

# Reading from a file

## Read the whole file at once

This code reads the entire contents of the file into the variable `data`.  

```
  with open('example.txt','r') as infile:
     data = infile.read()
```

If you want to treat the different lines of the file as separate lines after that, you could use this code
 to convert `data` to a list of strings called `lines`, one per line:

```
  lines = data.split("\n")
```

That's only a good idea if the file is relatively small.


# References

* Perkovic 2nd Edition (textbook), Section 4.3 (p. 107-116)
* [Python 3.6.5 docs section 7.2 on Input and Output Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* Examples of reading/writing files: <https://github.com/ucsb-cs8/python-text-files>
