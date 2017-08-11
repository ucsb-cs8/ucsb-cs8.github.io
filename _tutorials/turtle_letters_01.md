---
topic: "Turtle Letters: 01"
desc: "Draw a T"
indent: true
code_repo: https://github.com/ucsb-cs8-m17/Lecture3_0810
---

{% include turtle_letters_header.html %}

Here is some code that draws the letter T with a given width and height.

This code makes the assumption that your turtle is called `t`.


```
def drawT(width,height):
   '''
   draw a T
   assume turtle facing east (0), and leave it facing east
   assume pen is down
   no assumptions about position.
   '''
   t.forward (width)
   t.backward (width/2)
   t.right (90)
   t.forward (height)
   t.left(90)
```

Here's a full Python file that draws a T:

```
import turtle

t = turtle.Turtle()

def drawT(width,height):
   '''
   draw a T
   assume turtle facing east (0), and leave it facing east
   assume pen is down
   no assumptions about position.
   '''
   t.forward (width)
   t.backward (width/2)
   t.right (90)
   t.forward (height)
   t.left(90)

drawT(50,100)

```

{% include turtle_tutorial_table_of_contents.html %}
