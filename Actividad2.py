"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *
from freegames import square, vector
from random import randrange, choice

pick_random_color = lambda: choice(["green", "blue", "orange", "pink", 'purple'])
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Color list
food_colors = ['green', 'blue', 'yellow', 'purple', 'orange']
current_food_color = choice(food_colors)

def move_food():
    direction = [vector(10, 0),vector(-10, 0),vector(0, 10),vector(0, -10)]
    """Select randomly a position"""
    random_p = randrange(4)
    move = direction[random_p]
    new_p = food + move

    """The food dosen´t leave the limits"""
    if -200 < new_p.x < 190 and -200 < new_p.y < 190:
       food.move(move)

    """Update"""
    square(food.x, food.y, 9,'green')
    update()


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    global current_food_color
    
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        #Change food color randomly
        current_food_color = choice(food_colors)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')


    move_food()

   #Draw the food with the selected color
    square(food.x, food.y, 9, current_food_color)
    update()
    ontimer(move, 100)


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




