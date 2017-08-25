---
topic: 'main blocks"'
desc: 'All about that crazy looking if __name__=="__main__": thing that you see in some Python code'
---

# Learning about the `__name__=="__main__"` block

In order to make your Python code as reusable as possible, it is considered a good practice in Python to put all of the main code of your program inside an `if`
statement with this funny looking condition. (I have a few print statements just as placeholders to
show where the code goes):

```

if __name__=="__main__":
   print("This is where all the code goes, except for")
   print("function definitions, import statements and")
   print("initialization of global variables")

```

When you do this, it makes it easier to `import` the code you write into another file and resuse all of your function
definitions, even if you do NOT want to reuse the "main" code for your program.

For example, consider the two Python files below, with names as shown in the comments:

<table>
<tr>
<td markdown="1">

```
# convert1.py

def milesToKm(miles):
   return 1.609344 * miles
   
print("10 miles = ",milesToKm(10)," kilometers")
```

</td>
<td markdown="1">

```
# convert2.py

def kmToMiles(km):
   return km / 1.609344;
   
if __name__=="__main__":
   print("10 km = ",kmToMiles(10)," miles")
```

</td>
</tr>
</table>

Both of these programs work fine&mdash;see the output below.

Now, suppose we needed these functions in a third program called `myProgram.py` that's in the same directory (folder) as `convert1.py` and `convert2.py`.  Rather that copying and pasting, we could just import them, like this:

```
# myProgram.py

import convert1
import convert2

print("20 miles = ",convert1.milesToKm(20)," kilometers")
print("20 km = ",convert2.kmToMiles(20)," miles")


```
 
Great!  But there is a problem.    When we run the program, we get an extra line of output we don't want:

```
TODO TRANSCRIPT HERE
```

What we see is that the  funny looking `if` test inside `convert2.py` is helping us by preventing the `print` statements in that file from being run when the file is imported.   But, in `convert1.py`, the print statements are just "right there", which means they get run every time the file is run directly (e.g. from the "Run Module" command in `idle3`) AND when the file is imported via `import convert1`.  This is undesirable.  So, the solution is change `convert1.py1` so that apart from `import` and `def`, all code goes inside the `if __name__=="__main__":` block (or just "main block", for short.)

# Summary of what the main block is for:

The main block (set up via `if __name__=="__main__":` ) inside a file such as `myCode.py` prevents code inside of `myCode.py` from being run
when `myCode.py` is imported, e.g. via `import myCode`.   The code  in the main block is only carried out when the file is executed directly (e.g. via "Run Module" in `idle3`).

Other example of when a file is "directly executed" (and the main block is run) include these:
* Running with the `python3` unix command, e.g. `python3 myCode.py`
* Running with a [shebang](/topics/shebang/) (visit that link for more info).


The stuff under this funny looking `if` test is <em>skipped</em> any time your import your Python file (e.g. if this file is `foo.py
In this article, we'll discuss how you do this and why you do it.

# Guidelines:

Put all your code in a Python program inside a main block except for:
* import statements
* function definitions (anything starting with "def")
* initialization of global variables (if you are using them)
* class declarations (which you probably won't use in CMPSC 8).

Here's how it looks:

```
if __name__=="__main__":
   # code starts here
   # and is all indented
   print("this is a placeholder for your code")
   
```

Make sure you type that line with the `if`  <em>exactly</em> as shown:
* The variable `__name__` must be exactly two underscore characters, followed by exactly this: `name`, followed by exactly two underscore characters. 
* The string `"__main__"` must be exactly two underscore characters, followed by exactly this: `main`, followed by exactly two underscore characters.
* It must be exactly two equals signs: `==`
* The only part that can vary is whether you use single or double quotes. `'__main__'` or `"__main__"` are both ok.

