from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

window = Screen()
window.setup(600, 600)
window.title("snake game")
window.bgcolor("black")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

is_game_on = True

while is_game_on:
    snake.move()
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.right, "Right")
    window.onkey(snake.left, "Left")
    window.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        snake.extend()
        food.appear()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

    for segment in snake.turtles[: -1]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()



window.exitonclick()