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
