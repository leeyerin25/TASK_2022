from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0 . high score 를 텍스트로 저장해서 유기적저장이되는 하드디스크에 넣자. 방법은?
        with open("data.txt") as data : #with 쓰면 open후 close 할 필요 X\
            self.high_score = int(data.read()) #숫자로 계속 변경하고 싶으면 int 로 쓰자
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
               data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
