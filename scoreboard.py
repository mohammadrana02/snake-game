from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.speed("fastest")
        self.update_scoreboard()

    def read_high_score(self):
        """reads the high score from the data.txt file"""
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()

    def update_high_score(self):
        """reads the high score from the data.txt file"""
        with open("data.txt", mode="w") as file:
            file.write(str(self.score))

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 20, 'normal'))

    def reset(self):
        """rests the scoreboard and updates the high score if necessary"""
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score and updates the scoreboard"""
        self.score += 1
        self.clear()
        self.goto(x=0, y=270)
        self.update_scoreboard()
