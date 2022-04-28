from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def scoring(self, count):
        super().penup()
        super().goto(-50, 280)
        super().hideturtle()
        super().pencolor("white")
        super().write(f"Score = {count}", True, align="left", font=10)

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER", align="left", font=50)
