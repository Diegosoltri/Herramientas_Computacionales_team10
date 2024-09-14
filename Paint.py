"""Paint, para dibujar formas.

Este programa utiliza el módulo turtle para crear una aplicación interactiva de dibujo.

Permite a los usuarios:
1. Dibujar líneas, cuadrados, círculos, rectángulos, triángulos y pentágonos.
2. Cambiar el color de las formas dibujadas.
3. Deshacer la última acción.

Las formas se dibujan haciendo clic en el lienzo para definir los puntos de inicio y fin.

Ejercicios:
1. Añadir más colores.
2. Completar más formas.
3. Añadir un parámetro de ancho para ajustar el grosor de las líneas.
"""

from turtle import *
from freegames import vector
import math


def line(start, end):
    """Dibuja una línea desde el punto de inicio hasta el de fin."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Dibuja un cuadrado con la esquina superior izquierda en el punto de inicio
    y el tamaño determinado por el punto de fin."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle_(start, end):
    """Dibuja un círculo con el centro en el punto de inicio y el radio determinado por el punto de fin."""
    rad = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    center = start.y - rad

    up()
    goto(start.x, center)
    down()
    begin_fill()
    circle(rad)
    end_fill()


def rectangle(start, end):
    """Dibuja un rectángulo desde el punto de inicio hasta el de fin."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


def triangle(start, end):
    """Dibuja un triángulo equilátero con el lado determinado por la distancia entre el inicio y el fin."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def pentagon(start, end):
    """Dibuja un pentágono con el lado determinado por la distancia entre el inicio y el fin."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    side_length = end.x - start.x

    for _ in range(5):
        forward(side_length)
        left(72)

    end_fill()


def tap(x, y):
    """Almacena el punto de inicio o dibuja una forma dependiendo del estado actual."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Almacena un valor en el diccionario de estado."""
    state[key] = value


# Inicialización del estado y configuración
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)

# Manejadores de eventos
onscreenclick(tap)
listen()
onkey(undo, 'u')  # Deshacer última acción
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('violet'), 'V')

# Selección de formas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', pentagon), 'p')

# Finalización del programa
done()
