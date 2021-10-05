from turtle import Turtle, Screen

class WallTurtle(Turtle):
  def __init__(self, 
               x = -275, 
               y = -50):
    Turtle.__init__(self)
    self.shape("square")
    self.shapesize(3, 1, 1)

    # Sets up incoming variables
    self.x = x
    self.y = y
    self.window = Screen()

   #set turtle starting states
    self.shape("square")
    self.shapesize(1,3,1)
    self.color("black")
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
