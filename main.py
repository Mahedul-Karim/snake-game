from turtle import Turtle,Screen

screen = Screen()
screen.setup(550,550)
screen.bgcolor("black")
screen.title("Hungry Snake")

snake_positions = [(0,0),(-20,0),(-40,0)]

for position in snake_positions:
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.goto(position)


screen.exitonclick()