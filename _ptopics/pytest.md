---
topic: "pytest"
desc: "Unit Testing with the pytest module"
---

# Checking whether pytest is installed

To see whether pytest is installed, try this command:

```
python3 -m pytest
```

If pytest is installed, the output will look something like this:

```
-bash-4.3$ python3 -m pytest
===================================== test session starts ======================================
platform linux -- Python 3.4.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /cs/faculty/pconrad/cs8/lab02, inifile:
collected 0 items                                                                               

================================= no tests ran in 0.03 seconds =================================
-bash-4.3$ 
```

On a Mac, it looks like this:

```
Phills-MacBook-Pro:lab02 pconrad$ python3 -m pytest
====================================== test session starts ======================================
platform darwin -- Python 3.6.2, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /Users/pconrad/cs8/lab02, inifile:
collected 0 items                                                                                

================================= no tests ran in 0.00 seconds ==================================
Phills-MacBook-Pro:lab02 pconrad$ 
```

# Installing PyTest on your own system (or for your personal use on CSIL):

If you are working on CSIL, PyTest is likely already installed for you (check using the command shown above).

If not, use this command to install it for your own use:

```
pip3 install --user pytest
```

Then try the commands listed above.

# Running tests from a single file

To run tests from foo.py, use:

```
python3 -m pytest foo.py
```

To run only a particular test called `test_bar3`, use:

```
python3 -m pytest foo.py -k test_bar3
```

The `-k` does pattern matching, so it can also be a substring of a set of tests you want to run.   With suitable naming conventions,
you can have fine control over subsets of the test suite from the command line.

# Minimizing output

If you want the output from a set of tests to be compact, and the same each time you run them 
(e.g. for use with autograder system such as submit.cs) use the `-qq` flag:

```
python3 -m pytest -qq foo.py -k test_bar3
```
