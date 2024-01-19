"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)//2,
                            y=self.window_height-paddle_offset)
        self.window.add(self.paddle)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius, self.ball_radius, x=(self.window_width//2-self.ball_radius),
                          y=(self.window_height//2-self.ball_radius))
        self.window.add(self.ball)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.brick_num = brick_cols * brick_rows     # To control the ending of the game

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.change_position)
        self.is_begin = False
        onmouseclicked(self.ball_bouncing)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=BRICK_OFFSET+j*(brick_height+brick_spacing))
                if 0 <= j % BRICK_ROWS < 2:
                    self.brick.filled = True
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                if 2 <= j % BRICK_ROWS < 4:
                    self.brick.filled = True
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                if 4 <= j % BRICK_ROWS < 6:
                    self.brick.filled = True
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                if 6 <= j % BRICK_ROWS < 8:
                    self.brick.filled = True
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                if 8 <= j % BRICK_ROWS < 10:
                    self.brick.filled = True
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

    # Move the paddle
    def change_position(self, event):
        if event.x <= PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif event.x >= self.window_width - (PADDLE_WIDTH/2):
            self.paddle.x = self.window_width - PADDLE_WIDTH
        else:
            self.paddle.x = event.x - PADDLE_WIDTH/2
        self.paddle.y = self.window_height - PADDLE_OFFSET

    # Move the ball
    def ball_bouncing(self, event):
        self.is_begin = True  # Clicking mouse to turn on the switch of ball falling
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Get the ball's vx
    def get_vx(self):
        return self.__dx

    # Get the ball's vy
    def get_vy(self):
        return self.__dy

    # Reset the ball's original position
    def initial_statement(self):
        self.is_begin = False         # Turn on the switch of ball falling
        self.window.add(self.ball, x=(self.window_width//2-self.ball_radius),
                        y=(self.window_height//2-self.ball_radius))
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
