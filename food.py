import turtle as t 
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        t.colormode(255)
        self.penup()
        self.shape("turtle")
        self.colorsetter()
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.refresh()

    def colorsetter(self):
        r = random.randint(100,255)
        g = random.randint(100,255)
        b = random.randint(100,255)
        customcolor = (r, g, b)
        t.colormode(255)
        self.color(customcolor)


    def refresh(self):
        random_x =  random.randint(-280,280)
        random_y =  random.randint(-280,280)
        self.goto(random_x, random_y)
        self.colorsetter()
