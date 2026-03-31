from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(550,550)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)

snake_positions = [(0,0),(-20,0),(-40,0)]

body_segments = []

for position in snake_positions:
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(position)
    body_segments.append(snake_body)

game_started = True

while game_started:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(body_segments) - 1,0,-1):
        x_coords = body_segments[segment - 1].xcor()
        y_coords = body_segments[segment - 1].ycor()
        body_segments[segment].goto(x_coords,y_coords)
    body_segments[0].forward(20)


screen.exitonclick()