from turtle import Turtle

START_COR = [(0,0), (-20,0), (-40,0)]
FORWARD_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.CreateSnake()
        self.head = self.turtles[0]


    def CreateSnake(self):
        for i in range(len(START_COR)):
            newinstace = Turtle(shape= "square")
            newinstace.color("white")
            newinstace.penup()
            newinstace.goto(START_COR[i])
            self.turtles.append(newinstace)

    def MoveSnake(self):
        for i in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[i-1].xcor()
            new_y = self.turtles[i-1].ycor()
            self.turtles[i].goto(new_x,new_y)
        self.turtles[0].shape("arrow")
        self.turtles[0].color("Coral")
        self.turtles[0].forward(FORWARD_DISTANCE)


    def Up(self):
        if self.head.heading() != DOWN: self.head.setheading(UP) 


    def Down(self):
        if self.head.heading() != UP:   self.head.setheading(DOWN) 

    def Left(self):
        if self.head.heading()!= RIGHT:  self.head.setheading(LEFT) 

    def Right(self):
        if self.head.heading()!= LEFT: self.head.setheading(RIGHT) 


