import curses
import textwrap
import msgbox
from utils import center_position


def menu(con, root, header, options, width, screen_width, screen_height):
    #FIXME: use alphabets for hotkeys... going to fix
    if len(options) > 26:
        raise ValueError

    header_wrapped = textwrap.wrap(header, width)
    header_height = len(header_wrapped)
    height = len(options) + header_height

    pos_x, pos_y = center_position(width, height, screen_width, screen_height)
    win = curses.newwin(height, width, pos_y, pos_x)

    win.border()
    win.overlay(con)

    win.noutrefresh()
