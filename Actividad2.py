from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Función para cambiar la dirección de la serpiente
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

# Verifica si la cabeza de la serpiente está dentro de los límites
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# Función que mueve la comida de manera aleatoria un paso a la vez
def move_food():
    direction = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = choice(direction)
    newposition = food + move

    if -200 < newposition.x < 190 and -200 < newposition.y < 190:
        food.move(move)

# Función para mover la serpiente
def move():
    """Move snake forward one segment."""
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
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    
    move_food()  # Mover la comida en cada paso
    
    update()
    ontimer(move, 100)

# Configuración de la pantalla y controles
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
