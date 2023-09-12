from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt","r" ) as hs:
            self.highscore=int(hs.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score :{self.score}\t high score:{self.highscore}", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt","w") as hs:
                hs.write(f"{self.highscore}")

        self.update_score()
    #def game_over(self):
    #   self.goto(0,0)
    #   self.write("GAME OVER",align="center",font=("Arial",40,"normal"))