"""
File: bouncing_ball
Name:NIU
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
is_begin = False       # Set the switch of ball falling

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global is_begin
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    stop_point = 0                            # Variable to control the ending time
    onmouseclicked(start)
    vy = 0
    while True:
        pause(DELAY)
        if ball.x + SIZE >= window.width:     # The ball goes over the right boundary
            stop_point += 1
            vy = 0                            # Reset ball velocity
            window.remove(ball)
            window.add(ball, x=START_X, y=START_Y)   # Reset the position of the ball
            is_begin = False                  # Turn off the switch of ball falling
        if stop_point == 3:
            break                             # Ending time
        else:
            if is_begin:
                ball.move(VX, vy)
                if ball.y >= window.height:    # The ball is under the floor
                    vy = -vy*0.9               # The ball is bouncing
                else:
                    vy += GRAVITY              # The ball is falling


def start(event):
    global is_begin
    is_begin = True  # Clicking mouse to turn on the switch of ball falliing


if __name__ == "__main__":
    main()
