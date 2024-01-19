"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
first_v = False          # Check if it is the beginning of the ball falling, if yes, give the first vx,vy


def main():
    global first_v
    graphics = BreakoutGraphics()
    stop_point = 0  # variable to control the ending time
    ball = graphics.ball
    window = graphics.window
    vx = graphics.get_vx()
    vy = graphics.get_vy()

    # Add the animation loop here!
    count = 0                                # Count the brick to control the ending of the game
    while True:
        pause(FRAME_RATE)
        if ball.y >= window.height:          # When the ball exceeds the bottom boundary of the window
            stop_point += 1
            graphics.initial_statement()     # Reset the ball's original position
            first_v = False                  # It is going to be the beginning of the ball falling
        if stop_point == 3 or count == graphics.brick_num:
            # When the ball exceeds the bottom boundary of the window three times, Game Over!
            # When bricks are all removed, the game END!
            break
        elif graphics.is_begin:              # When click the mouse and turn on the switch of ball falling
            if not first_v:                  # The beginning of the ball falling, give the first vx,vy
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                ball.move(vx, vy)
                first_v = True               # It will not be the beginning of the ball falling, go to else
            else:
                ball.move(vx, vy)            # Check if the ball is bumping
                for i in range(2):
                    for j in range(2):
                        obj = graphics.window.get_object_at(graphics.ball.x+(graphics.ball_radius*i),
                                                            graphics.ball.y+(graphics.ball_radius*i))
                        if obj is not None:  # The ball is bumping
                            if obj is graphics.paddle:       # If the ball hits the paddle
                                vy = -vy                     # The ball change the moving y direction
                                ball.move(vx, vy)            # Avoid the situation that before the ball leave the
                                # paddle, it changes the moving direction again
                                break
                            else:                            # If the ball hits the brick
                                vy = -vy                     # The ball change the moving y direction
                                graphics.window.remove(obj)  # Remove the brick
                                count += 1                   # Calculate the number of the removed brick
                                break
            if graphics.ball.y <= 0:                         # If the ball touch the upper boundary of the window
                vy = -vy                                     # The ball change the moving y direction
            if graphics.ball.x <= 0 or graphics.window.width <= (graphics.ball.x + graphics.ball_radius):
                # If the ball touch the left of right boundary of the window
                vx = -vx                                     # The ball change the moving x direction


if __name__ == '__main__':
    main()
