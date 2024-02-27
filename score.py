from turtle import Turtle

FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 36, "normal")
PRESS_TO_CONTINUE_FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.clear()

        self.score = 0
        with open("Highscore.txt") as file:
            self.highscore = file.read()

        self.penup()
        self.hideturtle()
        self.color("white")
        
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=-160, y=260)
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def set_highscore(self):
        if self.score > int(self.highscore):
            with open("Highscore.txt", mode="w") as file:
                file.write(str(self.score))

    def game_over(self):
        self.goto(-125, 30)
        self.write(arg="GAME OVER", font=GAME_OVER_FONT)

        self.goto(-250, -50)
        self.write(arg="Press Space to continue", font=PRESS_TO_CONTINUE_FONT)

    def clear_score(self):
        self.clear()
