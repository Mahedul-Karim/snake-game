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
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.snake_head.xcor() > 270 or snake.snake_head.xcor() < -270 or snake.snake_head.ycor() > 270 or snake.snake_head.ycor() < -270:
        game_started = False
        scoreboard.game_over()

    for segment in snake.body_segments:

        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game_started = False
            scoreboard.game_over()
    


screen.exitonclick()