import turtle as t

ALIGNMENT = "center"
FFACE = "Poppins"
FSIZE = 8
FSTYLE = "bold"

FONT = (FFACE, FSIZE, FSTYLE)

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.sckore = 0
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.createScore()

    def createScore(self):
        self.write(arg= f"Score Board: {self.sckore}", align = ALIGNMENT, font=FONT)


    def UpdateScore(self):
        self.clear()
        self.sckore += 1
        self.createScore()

    def GameOver(self):
        self.goto(0,0)
        self.write("<GAME OVER>", font=FONT, align= ALIGNMENT )
