from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.speed("fastest")
        self.write(f"Score = {self.score}", True, align="center", font=("Courier", 20, 'normal'))

    def game_over(self):  # game over screen
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):  # increases the scoreboard
        self.score += 1
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score = {self.score}", True, align="center", font=("Courier", 20, 'normal'))
