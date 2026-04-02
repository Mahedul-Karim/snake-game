from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(550,550)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_started = True

while game_started:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    


screen.exitonclick()