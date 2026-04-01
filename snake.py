from turtle import Turtle

SNAKE_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_BY = 20

class Snake:

    def __init__(self):
        self.body_segments = []
        self.create_snake()

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(position)
            self.body_segments.append(snake_body)
    
    def move_snake(self):
        for segment in range(len(self.body_segments) - 1,0,-1):
            x_coords = self.body_segments[segment - 1].xcor()
            y_coords = self.body_segments[segment - 1].ycor()
            self.body_segments[segment].goto(x_coords,y_coords)
        self.body_segments[0].forward(MOVE_BY)