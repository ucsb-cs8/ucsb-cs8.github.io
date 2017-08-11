---
topic: "Turtle Letters: 04"
desc: "Planning your letters inside a bounding box (planning P and C)"
indent: true
---

{% include turtle_letters_header.html %}


For each letter that you and your pair partner are going to draw,
start by drawing a bounding box like this on on a piece of
paper. 

<img src="BoundingBox.png" title="BoundingBox.png" alt="BoundingBox.png" height="200" />

For example, consider my name: "Phill Conrad". I might plan out bounding
boxes like these.  Here, I've chosen each of the important points, and
labelled them. Note, though, that these are only examples. I don't
expect that everyone with a P or a C in their name will make the same
choices about how to shape the letters. In fact, I hope each of you
will make slightly different choices.

<img src="BoundingBoxP1.png" title="fig:BoundingBoxP1.png" alt="BoundingBoxP1.png" height="200" /> <img src="BoundingBoxC1.png" title="fig:BoundingBoxC1.png" alt="BoundingBoxC1.png" height="200" />

For instance, as an alternative, I might use bounding boxes like these:

<img src="BoundingBoxP2.png" title="fig:BoundingBoxP2.png" alt="BoundingBoxP2.png" height="200" /> <img src="BoundingBoxC2.png" title="fig:BoundingBoxC2.png" alt="BoundingBoxC2.png" height="200" />

Or even these, if I get ambitious, and want to try to make rounded shapes using the turtle's [circle](http://docs.python.org/3.3/library/turtle.html#turtle.circle) function (note: that's a link to the documentation!)

<img src="BoundingBoxP3.png" title="fig:BoundingBoxP3.png" alt="BoundingBoxP3.png" height="200" /> <img src="BoundingBoxC3.png" title="fig:BoundingBoxC3.png" alt="BoundingBoxC3.png" height="200" />

A warning about that last approach: although it may seem like it isn't that tough, there are some subtle traps. For example, in the C, what if we are drawing a short, fat C where height &gt; width? Then h-w will be negative, and there may be "issues". You might find that you would need more than one drawing, one for when (h-w)&gt;0, and a different approach when (h-w)&lt;0, and then use an if/else statement in your drawing code. It might be better to stick to approaches that don't involve interaction between height and width, which probably means straight lines. If you and your partner are up for the challenge of using curves and circles, you are welcome to try, but I advocate trying the straight line approach FIRST just to be safe.

Once you've planned your letters on paper, you are ready to start coding.

