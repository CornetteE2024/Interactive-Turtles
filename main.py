from turtle import Screen
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from movingturtle import MovingTurtle
from wallturtle import WallTurtle


# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance
button = ClickableTurtle()


wall_list = []

#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)
player_2 = KeyboardTurtle(window, "w", "d", "a", "s")

player_1.goto(-270,0)
player_2.goto(0,-100)

# set target of other player(our collison check) to the opposite player
player_1.other_player = player_2
player_2.other_player = player_1

moveT = MovingTurtle(screen_width)


# Make Wall turtle
wall_20 = WallTurtle(-160, 17.5, .75, 5)
wall_list.append(wall_20)
wall_21 = WallTurtle(-121, 77.5, 7, .75)
wall_list.append(wall_21)



wall_1 = WallTurtle(-275, -25, .75, 3.5)
wall_list.append(wall_1)
wall_2 = WallTurtle(0, 190, 1, 30)
wall_list.append(wall_2)
wall_3 = WallTurtle(0, -185, 1, 30)
wall_list.append(wall_3)
wall_4 = WallTurtle(-290, 0, 20, 1)
wall_list.append(wall_4)
wall_5 = WallTurtle(285, 0, 20, 1)
wall_list.append(wall_5)
wall_6 = WallTurtle(-275, 25, .75, 3.5)
wall_list.append(wall_6)
wall_7 = WallTurtle(-250, 45, 3, .75)
wall_list.append(wall_7)
wall_8 = WallTurtle(-230, 65, .75, 3)
wall_list.append(wall_8)
wall_9 = WallTurtle(-210, 85, 3, .75)
wall_list.append(wall_9)
wall_10 = WallTurtle(-230, 105, .75, 3)
wall_list.append(wall_10)
wall_11 = WallTurtle(-250, 125, 3, .75)
wall_list.append(wall_11)
wall_12 = WallTurtle(-210, 145, .75, 5)
wall_list.append(wall_12)

wall_13 = WallTurtle(-170, 105, 5, .75)
wall_list.append(wall_13)

wall_14 = WallTurtle(-200, -25, 5.25, .75)
wall_list.append(wall_14)
wall_15 = WallTurtle(-222.3, -67, .75, 3.3)
wall_list.append(wall_15)
wall_16 = WallTurtle(-245, -102, 4.5, .75)
wall_list.append(wall_16)
wall_17 = WallTurtle(-200, -155, 5, .75)
wall_list.append(wall_17)
wall_18 = WallTurtle(-180, -115, .75, 3)
wall_list.append(wall_18)
wall_19 = WallTurtle(-160, -127.5, 2.25, .75)
wall_list.append(wall_19)


# HAS TO BE LAST! (Below)
# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment