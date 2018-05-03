---
topic: "Turtle Graphics"
desc: "Some basics about turtle graphics"
---

To use turtle graphics in Python:

* Use `import turtle` at the top of your file
* DO NOT name your file `turtle.py` (or the `import turtle` will get confused.  Literally ANY other name is fine.)

The full reference for Turtle Graphics for Python 3 is here:

* <https://docs.python.org/3.6/library/turtle.html>

# Troubleshooting

## My graphics exit immediately!

This typically arises if you are running turtle graphics from a script at command line instead of inside of IDLE.

Try calling the method `.getscreen().exitonclick()` on your turtle.

```
fred = turtle.Turtle()
fred.turtle("turtle")
fred.forward(100)
fred.getscreen().exitonclick()
```
