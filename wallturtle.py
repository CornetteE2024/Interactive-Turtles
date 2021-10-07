from turtle import Turtle, Screen


class WallTurtle(Turtle):
  def __init__(self, x, y, x_size, y_size):
    Turtle.__init__(self)


    # Sets up incoming variables
    self.window = Screen()
    self.x = x
    self.y = y
    self.x_size = x_size
    self.y_size = y_size


   #set turtle starting states
    self.shape("square")
    self.shapesize(self.x_size, self.y_size)
    self.color("black")
    self.penup()
    self.goto(self.x, self.y)