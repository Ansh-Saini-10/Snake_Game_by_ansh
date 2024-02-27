from turtle import Turtle, Screen
import time

screen = Screen()
POSITIONS = ((0, 0), (-20, 0), (-40, 0))


class MySnake:
    def __init__(self):
        self.snake_segments = []
        self.make_snake()
        self.snake_head = self.snake_segments[0]

    def make_snake(self):
        for coordinates in POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(coordinates)
            self.snake_segments.append(snake)

    def animation(self):
        screen.update()
        time.sleep(0.1)

        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i-1].xcor()
            new_y = self.snake_segments[i-1].ycor()
            screen.tracer(0)
            self.snake_segments[i].goto(x=new_x, y=new_y)
            screen.update()
        self.snake_head.forward(20)
        screen.update()

    def up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_head.setheading(0)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=self.snake_segments[-1].xcor(), y=self.snake_segments[-1].ycor())
        self.snake_segments.append(new_segment)

    def collision_with_tail(self):
        for snake_segment in self.snake_segments[1:]:
            if self.snake_segments[0].distance(snake_segment) < 10:
                return True

    def clear_snake(self):
        for snake in self.snake_segments:
            snake.hideturtle()
    
    def pause(self):
        for snake in self.snake_segments:
            self.done()