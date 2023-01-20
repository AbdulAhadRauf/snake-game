import turtle as t
import random
from snake  import Snake
import time

my_screen = t.Screen()
my_screen.setup(height = 600, width= 600)
my_screen.bgcolor("Black")
my_screen.title("Snake Game")
my_screen.tracer(0)


snake = Snake()

my_screen.listen()
my_screen.onkeypress(snake.Up, "Up")
my_screen.onkeypress(snake.Down, "Down")
my_screen.onkeypress(snake.Left, "Left")
my_screen.onkeypress(snake.Right, "Right")


game_is_on= True
while game_is_on:
    
    my_screen.update()
    time.sleep(0.1)
    snake.MoveSnake()
    










my_screen.exitonclick()
