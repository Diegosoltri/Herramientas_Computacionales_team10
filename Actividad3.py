"""Pacman, juego clásico de arcade.

Ejercicios:

1. Cambiar el tablero.
2. Cambiar el número de fantasmas.
3. Cambiar la posición inicial de Pacman.
4. Hacer que los fantasmas sean más rápidos/lentos.
5. Hacer que los fantasmas sean más inteligentes.
"""

from random import choice
from turtle import *
from math import sqrt
from freegames import floor, vector

# Estado del juego y configuración inicial
state = {'score': 0}  # Puntaje del jugador
path = Turtle(visible=False)  # Turtle para dibujar el tablero
writer = Turtle(visible=False)  # Turtle para escribir el puntaje
aim = vector(5, 0)  # Dirección inicial de Pacman
pacman = vector(-40, -80)  # Posición inicial de Pacman
ghosts = [
    [vector(-180, 160), vector(5, 0)],  # Fantasma 1 (posición y dirección)
    [vector(-180, -160), vector(0, 5)],  # Fantasma 2
    [vector(100, 160), vector(0, -5)],  # Fantasma 3
    [vector(100, -160), vector(-5, 0)],  # Fantasma 4
]

# Mapa del juego (0 = muro, 1 = camino con punto, 2 = camino sin punto)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    """Dibuja un cuadrado en la posición (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Devuelve el índice de una posición en el mapa."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Verifica si una posición es válida (sin muro)."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Dibuja el tablero del juego."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def distance(p1, p2):
    """Devuelve la distancia euclidiana entre dos puntos."""
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def move():
    """Mueve a Pacman y a los fantasmas."""
    writer.undo()
    writer.write(state['score'])  # Actualiza el puntaje

    clear()

    # Mueve a Pacman si la posición es válida
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    # Verifica si Pacman ha comido un punto
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')  # Dibuja a Pacman

    # Mueve a los fantasmas
    for point, course in ghosts:
        if valid(point + course):
            point.move(course * 4)  # Mueve al fantasma
        else:
            # Cambia la dirección del fantasma
            options = [
                vector(5, 0),  # Derecha
                vector(-5, 0),  # Izquierda
                vector(0, 5),  # Arriba
                vector(0, -5),  # Abajo
            ]
            valid_options = [option for option in options if valid(point + option)]

            # Si hay opciones válidas, elige la mejor o una aleatoria
            if valid_options:
                best_move = min(valid_options, key=lambda option: abs((point + option).x - pacman.x) + abs(
                    (point + option).y - pacman.y))
                if choice([True, False]):  # 50% de probabilidad de moverse en una dirección aleatoria
                    best_move = choice(valid_options)

                course.x = best_move.x
                course.y = best_move.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')  # Dibuja al fantasma

    update()

    # Verifica si algún fantasma ha alcanzado a Pacman
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)  # Continua el movimiento cada 100 ms


def change(x, y):
    """Cambia la dirección de Pacman si es válida."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# Configuración inicial del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')  # Movimiento hacia la derecha
onkey(lambda: change(-5, 0), 'Left')  # Movimiento hacia la izquierda
onkey(lambda: change(0, 5), 'Up')  # Movimiento hacia arriba
onkey(lambda: change(0, -5), 'Down')  # Movimiento hacia abajo
world()  # Dibuja el mundo
move()  # Inicia el movimiento
done()
