from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        """Speed in x of red ball"""
        speed.x = (x + 200) / 25 * 3
        """Gravity force in red ball"""
        speed.y = (y + 200) / 25 * 1.5


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        shape("triangle")
        stamp()

    for target in targets:
        goto(target.x, target.y)
        color('purple')
        shape("triangle")
        stamp()

    if inside(ball):
        goto(ball.x, ball.y)
        color('pink')
        shape("square")
        stamp()

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    """Move targets"""
    for target in targets:
        """Speed of targets"""
        target.x -= 0.5

    """Move the ball and apply gravity"""
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    """Reposition the ball if it leaves the screen"""
    if not inside(ball):
        ball.x = -200
        ball.y = -200
        speed.x = 0
        speed.y = 0

    """Check collisions and keep targets on screen"""
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            """Reposition the target if it leaves the screen"""
            if target.x < -200:
                target.x = 200
                target.y = randrange(-150, 150)
            targets.append(target)

    draw()

    """Continue moving the goals"""
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

