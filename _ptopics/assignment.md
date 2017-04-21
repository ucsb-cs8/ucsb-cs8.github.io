---
topic: "assignment statements"
desc: "giving a value to a variable, e.g. x=5"
---

In Python, an assignment statement gives a value to a variable.

Here are three examples:

```
x=5
name="Chris"
temperature=98.6
```

The equals sign `=` appears in Python assignment statements, but it isn't used the same way as it is used in a Math class.  
For example, in a math class, the `=` sign is symmetric meaning that you can flip the right and left hand side.  In Math class, if $$x=y$$ then $$y=x$$.

But Python is different.  The left hand side of the `=` and right hand side of the `=` have different meanings.

* The left hand side, e.g. `x`, `name`, and `temperature` in the examples above, always indicates where a new value is going to be stored.
* The right hand side, e.g, `5`, `"Chris"`, and `98.6`, always indicates the value that gets stored.

If you are reading Python code out loud, or to yourself silently, it may help to read the `=` symbol as "get the value" rather than as "equals".

For example:

* `x=5` is pronounced: "x gets the value five" (not "x equals five")
* `name="Chris"` is pronounced: "name gets the string Chris" (not "name equals Chris")

# Elements of a list can appear on the left hand side

If you already know about lists, then it may be helpful to know that list elements can appear on the left hand side of an assignment
statement.  If you don't know about lists yet, skip over this section until later.

On the left hand side, you can put variables such `x`, `name`, `temperature`, as in the examples above.

You can also use expressions refer to elements of a list, such as `names[3]`.  For example:

```
names=[] 
names[0] = "Chris"    
names[1] = "Pat"
names[2] = "Hunter"
```
