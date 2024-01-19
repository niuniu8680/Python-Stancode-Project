"""
File: draw_line
Name: NIU
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the hole
SIZE = 10
s_p = GOval(SIZE, SIZE)
s_p.filled = True
s_p.fill_color = 'white'
s_p.color = 'black'
is_start = True         # Set the switch of drawing a line
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(starting_point)


def starting_point(event):
    global s_p, is_start
    if is_start:            # Create a point
        window.add(s_p, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
        is_start = False    # Turn on the switch of drawing a line
    else:                   # Draw a line
        line = GLine(s_p.x + SIZE / 2, s_p.y + SIZE / 2, event.x, event.y)
        window.add(line)
        window.remove(s_p)
        is_start = True      # Turn off the switch of drawing a line


if __name__ == "__main__":
    main()
