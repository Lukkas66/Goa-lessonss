from turtle import *

#we want to paint a house 

#step 1: draw a square

width(10)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("gray")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

penup()
goto(150, 150)
pendown()

color("red")
begin_fill()
left(30)
forward(20)
left(90)
forward(35)
right(270)
forward(40)
left(90)
forward(35 )
left(90)
forward(20)
end_fill()

#drawing second window

penup()
goto(30, 170)
pendown()

color("red")
begin_fill()
forward(35)
left(90)
forward(35)
right(270)
forward(35)
left(90)
forward(35)
end_fill()


exitonclick()

