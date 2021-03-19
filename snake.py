"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import os

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def skipEdge(object):
    if not inside(object):
        if object.x > 190:
            object.x = -200
        elif object.x < -200:
            object.x = 190
        elif object.y > 190:
            object.y = -200
        elif object.y < -200:
            object.y = 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    speed = len(snake)

    # Move food
    randNum = randrange(1,50)
    if randNum == 1:
      food.x = food.x -20
    if randNum == 49:
      food.y = food.y -20

    # Make snake go around the edges
    skipEdge(head)

    # Make the food go around the edges
    skipEdge(food)


    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, int(100/speed))

os.system('cls' if os.name == 'nt' else 'clear')
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
