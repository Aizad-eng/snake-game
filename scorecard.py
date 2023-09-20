from turtle import Turtle
SPACE ="                                    "
class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.high_score = self.read_high_score()
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

    def write_high_score(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            # Handle the case when the file does not exist
            self.high_score = 0

        return self.high_score

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            self.write_high_score()
        self.score = 0
        self.display_score()
