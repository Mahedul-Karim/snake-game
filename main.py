from turtle import Turtle,Screen
from snake import Snake
import time

screen = Screen()
screen.setup(550,550)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)

snake = Snake()

game_started = True

while game_started:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    


screen.exitonclick()