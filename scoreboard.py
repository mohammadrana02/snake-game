from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.speed("fastest")
        self.update_scoreboard()

    # def game_over(self):
    #     """game over screen"""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score and updates the scoreboard"""
        self.score += 1
        self.clear()
        self.goto(x=0, y=270)
        self.update_scoreboard()
