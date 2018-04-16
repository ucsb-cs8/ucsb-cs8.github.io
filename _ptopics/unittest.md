---
topic: "Python: unittest"
desc: "module for test-driven development in Python"
---

# Using `unittest` to test your Python code

Test-driven development involves writing "unit tests" for each individual
unit of code: typically each function definition.

Unit tests, or "test cases" as they are sometimes called, are specified
by:

* Writing a function call with an actual parameter (the actual result)
* Writing the value what we expect that function to return (the expected results)
* *Asserting* that those are equal to each other, i.e. `actual==expected`

Then, if `actual==expected`, the test cases passes, otherwise it fails.

In the case of tests involving decimals, we might instead assert that
the actual and expected are *almost equal*, meaning that the absolute
value of the difference between them is less than some small
value&mdash;or to say it another way, that they are equal within a
certain number of decimal places.

One way to write these test cases in Python is with a module that we can
import called `unittest`.  

As an example, consider this simple function that converts Fahrenheit
to Celsius, stored in `tempFuncs.py`

```
# tempFuncs.py
def ftoc(fTemp):
   return (fTemp - 32)*(5.0/9.0)
```

To write tests for this, we can put the following into a file called
`test_tempFuncs.py`.  (Note that we don't *have* to call the file `test_` followed by the name of the file we are testing, but that is a handy naming convention to follow.)

Following the code block, we provide an explanation one line at a time.

```
# test_tempFuncs.py

import unittest
from tempFuncs import ftoc

class Test_tempFuncs(unittest.TestCase):

   def test_ftoc_1(self):
      self.assertAlmostEqual(ftoc(212.0),100.0)

   def test_ftoc_2(self):
      self.assertAlmostEqual(ftoc(32.0),0.0)

   def test_ftoc_3(self):
      self.assertAlmostEqual(ftoc(-40.0),-40.0)

   def test_ftoc_4(self):
      self.assertAlmostEqual(ftoc(67.0),19.4444,places=3)

if __name__=="__main__":
    unittest.main()
```

# Line-by-line explanation

We now explain the contents of `test_tempFuncs.py` one or two lines at a time.


```
# test_tempFuncs.py
```

This line is merely a comment with the name of the file, for identification purposes.

```
import unittest
```

We must import `unittest` to be able to use the features provided in this module for unit testing.


```
from tempFuncs import ftoc
```

This line imports the function we want to test, `ftoc`, directly from the file `tempFuncs.py`.  We could also have written `import tempFuncs`, but then we'd have to write `tempFuncs.ftoc` each time we wanted to use the `ftoc` function.

```
class Test_tempFuncs(unittest.TestCase):
```

This first word on the line, `class`, indicates that what follows is a
`class` definition.  The name of the class is `Test_tempFuncs`, and the
part in parenthesis, `unittest.TestCase` indicates the *parent class* of
this one.    This class, `Test_tempFuncs` will *inherit* some features from
its parent, that makes it function properly as a TestCase.   

The concept of a `class` is one that we'll get into more
deeply later when we discuss object-oriented programming, and which
you'll explore much more deeply when you take CSE 8A or 11 in Java.

For now, it is enough to know two things&mdash;although this is vastly
oversimplified explanation and far from the full truth about what a class
is: 
* Know that a class is a collection of related function definitions.  
* Know that classes can *inherit* some capabilities from a parent class,
   so that we don't have to write *all* of the code they need to do some job.

In this case, all of the related function definitions are the ones that 
immediately follow the line that starts with `class ...`, and are indented
under it.    The class ends with the blank line just before the `if` test,
which is *not* indented.   The fact that the `if` test is not indented
indicates that it is the first line that is NOT part of the class.

Now we turn to the first function definition that is part of the class. Note that for every function that you write for testing purposes, the function name should start with "test_":

```
   def test_ftoc_1(self):
      self.assertAlmostEqual(ftoc(212.0),100.0)
```

In Python, each function that is part of class typically has, as its first
parameter, a special value called `self`.   For now, it is enough to know
that this special value has to be there, and it gives us access to some of 
the special feature we "inherit" from our parent.  

So, when we want to check whether `ftoc(212.0)` converts the Farenheit value
212.0 correctly to the Celsius value `100.0`, we write:

```
      self.assertAlmostEqual(ftoc(212.0),100.0)
```

We put this inside the function called `test_ftoc_1`, and we put that
function definition inside a class that inherits from unittest.TestCase.

We then add two more similar function definitions, for two additional
test cases.  Each one needs its own separate name.

```
   def test_ftoc_2(self):
      self.assertAlmostEqual(ftoc(32.0),0.0)

   def test_ftoc_3(self):
      self.assertAlmostEqual(ftoc(-40.0),-40.0)
```

Up until now, we expect the values to be either exactly equal, or very close
to exactly equal.  The `assertAlmostEqual` function, by default, compares
the absolute value of the difference to seven decimal places.  If we want to
compare to fewer or more, though we can override the default, as shown
in the last function definition of our sample code:

```
   def test_ftoc_4(self):
      self.assertAlmostEqual(ftoc(67.0),19.4444,places=3)
```

The class is now finished, and we have just two more lines of code.  This
first line of code is peculiar, but you'll see it a lot, and eventually get
used to it:

```
if __name__=="__main__":
    unittest.main()
```

The if test here is indeed strange.  What is `__name__`?  and what is `"__main__"`?  The answer is that this is a bit of a hack, a kludge&mdash;that is, a sort of inelegant solution to a problem.    In Python, a file can be run in at least two different ways:

1.  It can be "directly run"&mdash;that is, a user asked for this file
    by name to be run by selecting the "Run" menu option in idle3, for
    example, or by typing `python thisFile.py` at the unix command line.

2.  It can be "indirectly run" by being *imported* into another Python
    file that is directly run.  (That can also be several layers deep: it
    may be imported by a file, that is imported by a file, that is
    imported by a file ... that is directly run.)

Sometimes we want to know which one is happening, and run some code
ONLY in the case where the file is being "directly run".

That is what the line of code `if __name__ == "__main__" does.

Any time a file is being directly run, the `__name__` variable gets set to
the special value `"__main__"`.   

Any other time, it is set to the name of the module, which is the name
of the Python file without the `.py` on the end (e.g. for `foo.py`,
name is set to `foo`.

So in the end, the if test below just means "do this code only if this 
file is being directly run; if its being imported into another file,
skip this part."

```
if __name__=="__main__":
    unittest.main()
```

But what about the line `unittest.main()`?  That line is the part that
*actually runs the tests*.  The `main()` function is part of the `unittest`
module. What it does is look for any and all classes that inherit from
`unittest.TestCase` that it can find, and runs every single test case
from every single one of them.   The code that prints out how many tests
pass and fail is part of that `unittest.main()` function.

