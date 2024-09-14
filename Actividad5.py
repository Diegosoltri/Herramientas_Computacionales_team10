from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
"""Lista de símbolos en lugar de números para las fichas."""
symbols = ['@', '#', '£', '∞', '$', '%', '&', '!', '*', '+', '-', '/', '?', '§', '♥', '♦', '♣', '♠', '©', '®', '✓', '★',
           '☺', '☻', '☼', '☽', '⚽', '⚾', '♫', '♪', '♥', '♦']
tiles = symbols * 2  # Crear una lista duplicada de símbolos para emparejarlos.
state = {'mark': None}  # Estado que almacena la posición de la ficha marcada.
hide = [True] * 64  # Lista que mantiene el estado de cada ficha (oculta o visible).
tap_count = 0  # Contador de taps (toques de pantalla).


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en las coordenadas (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x, y) a un índice de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte el índice de las fichas en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza la ficha marcada y revela fichas según el tap (toque en pantalla)."""
    global tap_count  # Se utiliza para modificar la variable global del contador de taps.
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot  # Marca la ficha seleccionada si no hay coincidencia.
    else:
        hide[spot] = False  # Revela la ficha si hay coincidencia.
        hide[mark] = False  # Revela la ficha marcada previamente.
        state['mark'] = None  # Reinicia la marca.

    tap_count += 1  # Incrementa el contador cada vez que se hace un tap.


def revealed():
    """Devuelve True si todas las fichas están descubiertas, False de lo contrario."""
    return all(not h for h in hide)


def draw():
    """Dibuja la imagen del coche y las fichas en el tablero."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()  # Coloca la imagen del coche en el centro del tablero.

    # Dibuja las fichas ocultas en el tablero.
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # Si hay una ficha marcada y está oculta, muestra el símbolo.
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 10)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    # Dibuja el contador de taps en la esquina superior izquierda.
    up()
    goto(-200, 200)
    color('black')
    write(f"Contador: {tap_count}", align="left", font=("Arial", 12, "normal"))

    # Si todas las fichas están reveladas, muestra un mensaje de victoria.
    if revealed():
        up()
        goto(-200, -250)
        write("HAS DESTAPADO TODOS LOS CUADROS", align="left", font=("Arial", 14, "bold"))

    update()  # Actualiza el dibujo en la pantalla.
    ontimer(draw, 100)  # Llama a la función draw cada 100 milisegundos.


# Baraja los símbolos para las fichas.
shuffle(tiles)

# Configuración de la ventana de Turtle.
setup(420, 550, 370, 0)
addshape(car)
hideturtle()
tracer(False)

# Asignación de eventos.
onscreenclick(tap)
draw()
done()
