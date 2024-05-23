from turtle import *

#drawing house with garage

speed(10)

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)

# Set the background color for the sky
screen.bgcolor("skyblue")

# Draw the grass
penup()
goto(-400, -200)
pendown()
begin_fill()
color("green")
goto(400, -200)
goto(400, -600)
goto(-400, -600)
goto(-400, -200)
end_fill()
penup()

#drawing house 

penup()
goto(-300, -200)
pendown()

begin_fill()
width(5)
color("black")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

color("gray")
forward(600)
left(90)
forward(300)
left(90)
forward(400)
left(90)
forward(303)
left(90)
forward(170)
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
end_fill()

#drawing window 1

penup()
goto(200, 35)
pendown()

color("white")
forward(55)
left(90)
forward(45)
left(90)
forward(55)
left(90)
forward(45)

#drawing window 2

penup()
goto(1, 35)
pendown()

color("white")
forward(45)
left(90)
forward(55)
left(90)
forward(45)
left(90)
forward(55)


penup()
goto(-220, -200)
pendown()

begin_fill()
color("black")
forward(10)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)
end_fill()


#split garage and house

color("gray")
right(180)
forward(120)
color("black")
left(90)
forward(200)
left(90)
forward(200)

#adding 2 floor

color("gray")
begin_fill()
right(90)
forward(100)
right(90)
forward(600)
left(90)
forward(200)
left(90)
forward(600)
left(90)
forward(300)
end_fill()
color("black")
left(90)
forward(200)
left(90)
forward(100)
right(90)
forward(400)
left(90)
forward(200)
left(90)
forward(600)
left(90)
forward(300)

#second     floor windows

penup()
goto(200, 250)
pendown()

color("black")
right(90)
forward(400)
left(90)
forward(50)
left(90)
forward(400)
left(90)
forward(50)

exitonclick()