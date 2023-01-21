import turtle as t
from snake  import Snake
import time
from food import Food
from scoreboard import ScoreBoard


my_screen = t.Screen()
my_screen.setup(height = 600, width= 600)
my_screen.bgcolor("Black")
my_screen.title("Snake Game")
my_screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()


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
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_segment()
        scoreboard.UpdateScore() 

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.GameOver()
    
    for i in snake.turtles[1:]:
        if snake.head.distance(i) < 10:
            my_screen.update()
            game_is_on = False
            scoreboard.GameOver()


my_screen.exitonclick()
