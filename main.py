from turtle import Screen
from snake import MySnake
from food import Food
from score import Scoreboard
import random

my_bg_colors = ["#000", "#337357", "#FF3EA5", "#1D2B53", "#900C3F", "#FAA300", "#2e4242"]
my_food_colors = ["#FF004D", "#6420AA"]

def change_bg_color(colors: list) -> str: 
    chosen_color = random.choice(colors)
    return chosen_color


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(change_bg_color(my_bg_colors))
screen.title("Snake Game by Ansh")

snake = MySnake()
food = Food()
food.color(change_bg_color(my_food_colors))

score = Scoreboard()

def reset():
    score.clear()
    score.__init__()
    snake.clear_snake()
    snake.__init__()


screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")


def restart_game():
    reset()
    game()

def game():
    snake.animation()
    snake.increase_speed_by_points(score.score)

    # ================================== Detecting Collision with wall ==============================
    if snake.collision_with_wall(max_x=385, min_x=-385, max_y=285, min_y=-285):
        score.game_over()
        score.set_highscore()

        return

    # ================================== Detecting Collision with tail ==============================
    if snake.collision_with_tail():
        score.game_over()
        score.set_highscore()
        return

    # ======================================= Detecting Food ========================================
    if snake.snake_head.distance(food) < 20:
        food.teleport()
        screen.tracer(0)
        snake.extend()
        screen.update()
        score.increase_score()

        screen.bgcolor(change_bg_color(my_bg_colors))
        food.color(change_bg_color(my_food_colors))

    return game()


game()

screen.onkey(fun=restart_game, key="space")


screen.exitonclick()
