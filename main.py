from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#  screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns the screen animations off

#  creates the snake, food and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# controls for the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # updates the screen after all the segments have been generated
    time.sleep(0.1)  # refreshes the page after every 1/10 of a second

    snake.move()  # default snake movement

    # detect collision with food
    if snake.head.distance(food) < 15:  # if snake head is within 15 pixels of the food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()


screen.exitonclick()
