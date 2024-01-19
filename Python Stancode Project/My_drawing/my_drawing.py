"""
File: Reading_code
Name: NIU
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Winnie The Pooh sticker

    Winnie The Pooh is one of my favorite cartoon characters.
    Guess what the original sticker looks like?
    """
    window = GWindow(width=800, height=400)

    shirt = GRect(106, 80, x=307, y=180)
    window.add(shirt)
    shirt.filled = True
    shirt.fill_color = 'red'
    shirt.color = 'red'

    face = GOval(120, 110, x=300, y=100)
    window.add(face)
    face.filled = True
    face.fill_color = 'yellow'

    paper = GRect(50, 49, x=350, y=190)
    window.add(paper)
    paper.filled = True
    paper.fill_color = 'white'

    l_ear = GOval(30, 30, x=310, y=80)
    window.add(l_ear)
    l_ear.filled = True
    l_ear.fill_color = 'yellow'
    l_ear.color = 'yellow'

    r_ear = GOval(30, 32, x=390, y=83)
    window.add(r_ear)
    r_ear.filled = True
    r_ear.fill_color = 'yellow'
    r_ear.color = 'yellow'

    l_eyebrow = GRect(30, 3, x=319, y=125)
    window.add(l_eyebrow)
    l_eyebrow.filled = True
    l_eyebrow.fill_color = 'brown'
    l_eyebrow.color = 'brown'

    r_eyebrow = GRect(28, 3.5, x=380, y=127)
    window.add(r_eyebrow)
    r_eyebrow.filled = True
    r_eyebrow.fill_color = 'brown'
    r_eyebrow.color = 'brown'

    l_eye = GOval(5, 5, x=335, y=140)
    window.add(l_eye)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    l_eye.color = 'black'

    r_eye = GOval(5.5, 5.5, x=393, y=142)
    window.add(r_eye)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    r_eye.color = 'black'

    nose = GOval(23, 28, x=359, y=150)
    window.add(nose)
    nose.filled = True
    nose.fill_color = 'black'
    nose.color = 'black'

    mouth = GArc(13, 5, 270, 350)
    window.add(mouth, x=367, y=184)
    mouth.filled = True
    mouth.fill_color = 'black'
    mouth.color = 'black'

    l_hand = GOval(16, 20, x=400, y=210)
    window.add(l_hand)
    l_hand.filled = True
    l_hand.fill_color = 'yellow'
    l_hand.color = 'yellow'

    r_hand = GOval(28, 20, x=325, y=220)
    window.add(r_hand)
    r_hand.filled = True
    r_hand.fill_color = 'yellow'
    r_hand.color = 'yellow'

    belly_arc = GArc(115, 40, 0, 180)
    window.add(belly_arc, x=305, y=247)
    belly_arc.filled = True
    belly_arc.fill_color = 'yellow'
    belly_arc.color = 'yellow'

    belly1 = GOval(110, 50, x=305, y=240)
    window.add(belly1)
    belly1.filled = True
    belly1.fill_color = 'yellow'
    belly1.color = 'yellow'

    belly2 = GRect(109, 50, x=306, y=250)
    window.add(belly2)
    belly2.filled = True
    belly2.fill_color = 'yellow'
    belly2.color = 'yellow'


if __name__ == '__main__':
    main()
