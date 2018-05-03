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

There are at least two ways to resolve this.

(1) In the Python code, try calling the method `.getscreen().exitonclick()` on your turtle.

   ```
   fred = turtle.Turtle()
   fred.turtle("turtle")
   fred.forward(100)
   fred.getscreen().exitonclick()
   ```
(2) When running the Python code at the Unix shell prompt, use `python3 -i myprogram.py` instead of `python3 myprogram.py`.   
   ```
   $ python3 -i myprogram.py
   >>>
   ```
   Python will run your program, then drop you to a `>>>` prompt where you can type additional commands.
   That `>>>` prompt keeps the turtle variable alive, which keeps the Turtle graphics on the screen.  It also
   means you can interact with the drawing by checking the current position of the turtle, drawing additional stuff, etc.
   
   
