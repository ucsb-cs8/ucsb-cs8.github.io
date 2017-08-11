---
topic: "Turtle Letters: 02"
desc: "The bounding box, reference point, and Drawing an O (letter O as in Oscar, or zero as in 2000)"
indent: true
code_repo: https://github.com/ucsb-cs8-m17/Lecture3_0810
---

{% include turtle_letters_header.html %}

# The letter `O` as in `Oscar`, or zero as in `2000`

For any letter or number we draw, if we want to be able to combine it
with other letters and numbers, we are going to have to consider it to
have some "width" and some "height".

We are also going to consider something called the "reference point",
and something called the "bounding box".  The following illustration
shows this:

[[File:BoundingBox.png|x200px]]

![a](312px-ZeroInBoundingBoxv03.png)

![a](379px-BoundingBox.png)

![a](379px-ZeroInBoundingBoxVersion01.png)

![a](379px-ZeroInBoundingBoxv02.png)

![a](File-ZeroInBoundingBoxVersion01.png)


Now, inside this bounding box, we are going to draw our letter, or number, or symbol.

Let's consider a zero..

There are a number of ways to draw a zero, and at first we want to KEEP THINGS SIMPLE.

That is, do the simplest thing that will be recognizable as the shape of the letter or number we have in mind.

Later, if we want to get fancier, we can, but at first, KEEP THINGS SIMPLE.  At least on your first try, do the SIMPLEST THING THAT COULD POSSIBLY WORK.  This is a mantra that successful programmers often repeat to themselves.

So, here's a very simple zero.  It's nothing more than a rectangle, really.

[[File:ZeroInBoundingBoxVersion01.png|x200px]]

And the Python code to produce it is very simple.  Note that:
* We will assume the turtle starts at the reference point, facing right (heading 0), and with the pen down, and...
* We will leave the turtle facing right (0 degrees) at the lower right corner of the box, with the pen down.

<pre>
# draw digit zero as an example to show how letters might be drawn.
# P. Conrad for CS8, 10/08/2013

import turtle

def drawZero(aTurtle,width,height):
    """
    Draw the digit zero.  Assumes aTurtle starts pointing right,
    pen down
    at lower left of a rectantgle, with given width and height.

    Leave the turtle pointing right at the lower right of that
    same rectangle when done, with pen still down.
    """

    # Go counter-clockwise around the box
    
 
    aTurtle.forward(width)
    aTurtle.left(90)
    aTurtle.forward(height)
    aTurtle.left(90)
    aTurtle.forward(width)
    aTurtle.left(90)
    aTurtle.forward(height)
    aTurtle.left(90)
    
    # Now move over to lower left corner

    aTurtle.up(); aTurtle.forward(width); aTurtle.down()

def go():
    """
    Try out a few zeros.  Assumes we've already got a turtle named Fred.
    """
    drawZero(fred,30,60)

    fred.up()
    fred.forward(20)
    fred.down()

    drawZero(fred,15,45)

# This code creates the turtle "Fred" anytime we run this file.
# It gets executed every time because it is outside all the function definitions

fred = turtle.Turtle()
    
</pre>

To run this program, in IDLE, do:

* From File menu, choose New
* Paste in the Code
* Use Run (or hit F5) to run the code (you'll have to save, just like in lab00)
* At the Python prompt, type go() to see the Turtle do its thing.

But those zeros don't look much like zeros.  We can do a little better, with just a little bit of work.

Let's try clipping the corners a little to make the zero just a "little bit" rounder, and then give each of the important points a name:

{|
|[[File:ZeroInBoundingBoxv02.png|x200px]]
|[[File:ZeroInBoundingBoxv03.png|x200px]]
|}


