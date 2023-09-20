from turtle import Turtle
SPACE ="                                    "
class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.high_score = 0
        self.color("white")
        self.goto(-250,260)
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} {SPACE} High Score: {self.high_score}", move=False, align="Left", font=("Times New Roman",20,"bold"))
    def increment_score(self):
        self.score+=1
        self.display_score()
        print(self.score)

    def game_over(self):
        self.color("white")
        self.goto(-30,30)
        self.penup()
        self.hideturtle()
        self.write(f"Game-Over", move=False, align="center", font=("Arial", 20, "bold"))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score = 0
        self.display_score()
