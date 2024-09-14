from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)  # Posición inicial de la bola
speed = vector(0, 0)  # Velocidad inicial de la bola
targets = []  # Lista que almacena los objetivos en movimiento


def tap(x, y):
    """Responde al toque en la pantalla (tap).

    Si la bola no está en el área visible, se reposiciona en (-199, -199) y se ajusta la velocidad
    basada en la posición del toque.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Ajusta la velocidad de la bola en el eje x
        speed.x = (x + 200) / 25 * 3
        # Ajusta la velocidad de la bola en el eje y con una gravedad simulada
        speed.y = (y + 200) / 25 * 1.5


def inside(xy):
    """Devuelve True si el vector xy está dentro de la pantalla.

    El área visible es de (-200, -200) a (200, 200).
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja la bola y los objetivos en la pantalla."""
    clear()

    # Dibuja cada objetivo en la pantalla
    for target in targets:
        goto(target.x, target.y)
        shape("triangle")
        stamp()

    # Dibuja la bola si está dentro del área visible
    if inside(ball):
        goto(ball.x, ball.y)
        color('pink')
        shape("square")
        stamp()

    update()  # Actualiza la pantalla


def move():
    """Mueve la bola y los objetivos.

    Agrega nuevos objetivos en la pantalla y actualiza la posición de la bola y los objetivos,
    aplicando gravedad a la bola.
    """
    # Agrega un nuevo objetivo al azar cada 40 ciclos
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)  # Objetivo en el borde derecho
        targets.append(target)

    # Mueve los objetivos hacia la izquierda
    for target in targets:
        target.x -= 0.5

    # Mueve la bola si está dentro del área visible y aplica la gravedad
    if inside(ball):
        speed.y -= 0.35  # Gravedad aplicada a la velocidad en el eje y
        ball.move(speed)

    # Reposiciona la bola si sale de la pantalla
    if not inside(ball):
        ball.x = -200
        ball.y = -200
        speed.x = 0
        speed.y = 0

    # Mantiene los objetivos en pantalla y verifica colisiones con la bola
    dupe = targets.copy()  # Copia de la lista de objetivos
    targets.clear()

    for target in dupe:
        # Verifica si la bola está lo suficientemente cerca del objetivo (colisión)
        if abs(target - ball) > 13:
            # Reposiciona el objetivo si sale de la pantalla
            if target.x < -200:
                target.x = 200
                target.y = randrange(-150, 150)
            targets.append(target)  # Añade el objetivo de vuelta a la lista

    draw()  # Dibuja la escena actualizada

    # Continúa moviendo los objetivos cada 50 milisegundos
    ontimer(move, 50)


# Configuración inicial de la ventana Turtle
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)

# Asigna la función tap para que se active al hacer clic en la pantalla
onscreenclick(tap)

# Inicia el movimiento
move()

# Finaliza la ejecución de Turtle
done()
