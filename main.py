import time
from turtle import Screen
from snake import Snake
from food import Food
from scorecard import ScoreCard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.update()


snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right,"Right")



score=ScoreCard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() > 300 or snake.head.xcor()<-300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset_snake()
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.increment_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset_score()
            score.game_over()
            game_is_on = False


screen.exitonclick()