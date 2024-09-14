"""Snake, juego clásico de arcade.

Ejercicios:

1. ¿Cómo harías para que la serpiente se mueva más rápido o más lento?
2. ¿Cómo puedes hacer que la serpiente rodee los bordes del tablero?
3. ¿Cómo harías para que la comida se mueva?
4. Cambia el comportamiento de la serpiente para que responda a clics del mouse.
"""

from random import randrange, choice
from turtle import *
from freegames import square, vector

# Función lambda para seleccionar un color aleatorio
pick_random_color = lambda: choice(["green", "blue", "orange", "pink", 'purple'])

# Inicialización de la posición de la comida y la serpiente
food = vector(0, 0)  # La comida comienza en la posición (0, 0)
snake = [vector(10, 0)]  # La serpiente comienza con una longitud de 1 en la posición (10, 0)
aim = vector(0, -10)  # Dirección inicial de la serpiente (abajo)

# Lista de colores disponibles para la comida
food_colors = ['green', 'blue', 'yellow', 'purple', 'orange']
current_food_color = choice(food_colors)  # Color inicial de la comida

def move_food():
    """Mueve la comida a una nueva posición aleatoria en el tablero.

    La comida se moverá en una dirección aleatoria, pero se asegura de que no salga
    de los límites del tablero.
    """
    # Direcciones posibles para mover la comida
    direction = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    random_p = randrange(4)  # Selecciona una dirección aleatoria
    move = direction[random_p]
    new_p = food + move

    # Asegura que la comida no salga de los límites del tablero
    if -200 < new_p.x < 190 and -200 < new_p.y < 190:
        food.move(move)

    # Dibuja la comida en su nueva posición
    square(food.x, food.y, 9, 'green')
    update()


def change(x, y):
    """Cambia la dirección de la serpiente.

    La dirección de la serpiente se ajusta según los valores x e y recibidos.
    """
    aim.x = x
    aim.y = y


def inside(head):
    """Verifica si la cabeza de la serpiente está dentro de los límites del tablero.

    Devuelve True si la cabeza de la serpiente está dentro de los límites,
    False si está fuera.
    """
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente un segmento hacia adelante.

    Actualiza la posición de la serpiente y verifica si ha comido la comida.
    Si la serpiente choca consigo misma o sale de los límites, el juego termina.
    """
    global current_food_color

    head = snake[-1].copy()  # Copia la cabeza actual de la serpiente
    head.move(aim)  # Mueve la cabeza en la dirección actual

    # Verifica si la serpiente ha chocado consigo misma o ha salido de los límites
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Dibuja la cabeza en rojo si ha perdido
        update()
        return  # Termina el juego

    snake.append(head)  # Añade la nueva cabeza al cuerpo de la serpiente

    # Verifica si la serpiente ha comido la comida
    if head == food:
        print('Snake:', len(snake))  # Imprime la longitud de la serpiente
        food.x = randrange(-15, 15) * 10  # Nueva posición aleatoria de la comida
        food.y = randrange(-15, 15) * 10
        current_food_color = choice(food_colors)  # Cambia el color de la comida
    else:
        snake.pop(0)  # Elimina el último segmento de la serpiente si no ha comido

    clear()  # Limpia el tablero

    # Dibuja el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, 'black')

    # Mueve la comida a una nueva posición y la dibuja
    move_food()

    # Dibuja la comida con el color actual
    square(food.x, food.y, 9, current_food_color)
    update()  # Actualiza la pantalla

    # Repite la función move después de 100 ms
    ontimer(move, 100)


# Configuración inicial de la ventana de Turtle
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Control de la serpiente con las flechas del teclado
listen()
onkey(lambda: change(10, 0), 'Right')  # Mueve la serpiente a la derecha
onkey(lambda: change(-10, 0), 'Left')  # Mueve la serpiente a la izquierda
onkey(lambda: change(0, 10), 'Up')  # Mueve la serpiente hacia arriba
onkey(lambda: change(0, -10), 'Down')  # Mueve la serpiente hacia abajo

# Inicia el movimiento de la serpiente
move()

# Finaliza la ejecución de Turtle
done()
