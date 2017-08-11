---
topic: "Turtle Letters"
desc: "Drawing Letters of the Alphabet with Turtle Graphics"
---

This is a set of tutorial examples for drawing letters of the alphabet
and other symbols with Turtle Graphics.

A few hints in general about Turtle Graphics:

1. To make a turtle, we use `import turtle`, then an assignment statement that
   invokes the turtle constructor (`turtle.Turtle())` and gives the resulting turtle
   a name like `chris`:

   ```
   import turtle

   chris = turtle.Turtle()

   ```

2. To make a turtle "look like a turtle", use `t.shape("turtle")`, where `t` is the variable
   that refers to your turtle.  For example:

   ```
   chris.shape("turtle")
   ```

3. To move the turtle someplace without leaving a trail, pick up the pen, use `goto` to move,
   then put the pen down again.  For example, to get to `(25,50)` without leaving a trail, for a
   a turtle referred to as `chris`, you can do this:

   ```
   chris.up()
   chris.goto(25,50)
   chris.down()
   ```

<style>
div.tutorial-table * table { border-collapse: collapse; }
div.tutorial-table * table * th { border: 1px solid black; padding: 4px; }
div.tutorial-table * table * td { border: 1px solid black; padding: 4px; }
</style>

{% include turtle_tutorial_table_of_contents.html %}

