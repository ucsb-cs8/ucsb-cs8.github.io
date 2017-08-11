---
topic: "Turtle Letters: 02"
desc: "Drawing an A"
indent: true
code_repo: https://github.com/ucsb-cs8-m17/Lecture3_0810
---

<div style="display:none;">https://ucsb-cs8.github.io/tutorials/turtle_letters_02/
</div>

{% include turtle_letters_header.html %}


Instead of using `forward()` and `backward()`, another way to draw with turtle graphics is to calculate the exact points that make up the thing we want to draw, then just connect the dots.    

The following code creates a turtle called `someOlTurtle`:

```
import turtle

someOlTurtle = turtle.Turtle()
```

The following code can then be used to determine the current location of someOlTurtle.  At the start of a program, that's
always `(0,0)`, but later in a program, our turtle could be anywhere.   

```
startX = someOlTurtle.xcor()
startY = someOlTurtle.ycor()
```

<div style="float:right; width: 450px;margin:1em;" markdown="1">

| A in bounding box |
|-------------------|
|  ![A in bounding box](A_in_Bounding_Box_Turtle_Graphics_400.png) |

</div>

Setting `startx` and `starty` to the place the turtle starts out gives us a <em>reference point</em> for our letter.  We'll assume that reference point is at the lower left of the
letter we want to draw.   So for example, we'll assume that if we want to draw a `A` with a given width and height, that
it is going to be in a so-called "bounding box", with the reference point at the lower left, as shown in the picture at right labelled "A in bounding box".

<div style="clear: both;">
</div>

<div style="float:right; width: 450px; margin:1em;" markdown="1">

| A in bounding box with distances |
|----------------------------------|
| ![A in bounding box with distances](A_in_Bounding_Box_with_distances_400.png) |

</div>

We can then compute the vertical and horizontal distances to the various points that make up the lines that we'll use to draw the A, as shown here in the box at right labelled "A in bounding box with distances".


<div style="clear: both; margin-bottom: 1em;">
</div>


<div style="float:right; width: 450px; margin: 1em;"  markdown="1">

| A in bounding box with points |
|----------------------------------|
| ![A in bounding box with points](A_in_Bounding_Box_with_points_400.png) |

We can then label all the points as shown in the box at right labelled "A in bounding box with points".

</div>

It's helpful to give the x and y coordinates of each of the points a name,
as shown in the diagram "A in bounding box with points".

<div style="clear: both;">
</div>

By putting that altogether, we can, at last erite Python code to calculate the x and y values for those points in terms of the values `startX`, `startY`, `width` and `height`:

```
topAX = startX + (width/2)
topAY = startY + height

bottomRightX = startX + width
bottomRightY = startY
    
barLeftX = startX + width/4
barLeftY = startY + height/2

barRightX = startX + (width/4) + (width/2)
barRightY = startY + height/2
```


That gives us a way to draw the whole A, as shown here:

```
import turtle

someOlTurtle = turtle.Turtle()

def drawA(width, height):
    """
    someOlTurtle will draw the letter A with a given width and height,
    with the current location being the lower left corner of the A.
    """

    # figure out where we are

    startX = someOlTurtle.xcor()
    startY = someOlTurtle.ycor()

    # figure out the other points using only what we know,
    # which is width, height, startX and startY
    
    topAX = startX + (width/2)
    topAY = startY + height

    bottomRightX = startX + width
    bottomRightY = startY
    
    barLeftX = startX + width/4
    barLeftY = startY + height/2

    barRightX = startX + (width/4) + (width/2)
    barRightY = startY + height/2
    
    # draw left hand side of the A    
    someOlTurtle.goto(topAX,topAY)

    # draw the right side of the A

    someOlTurtle.goto(bottomRightX, bottomRightY)

    # draw bar across the middle
    
    someOlTurtle.up()
    someOlTurtle.goto(barLeftX,barLeftY)
    someOlTurtle.down()
    someOlTurtle.goto(barRightX,barRightY)

    # leave turtle at lower right hand corner of letter
    
    someOlTurtle.up()
    someOlTurtle.goto(bottomRightX,bottomRightY)
    someOlTurtle.down()
```

You'll notice that we left the turtle facing right at the right hand corner of the letter.
That's helpful in terms of being able to draw a series of letters going left to right.

{% include turtle_tutorial_table_of_contents.html %}
