import curses
import textwrap
import msgbox


def menu(con, root, header, options, width, screen_width, screen_height):
    #FIXME: use alphabets for hotkeys... going to fix
    if len(options) > 26:
        raise ValueError

    header_wrapped = textwrap.wrap(header, width)
    header_height = len(header_wrapped)
    height = len(options) + header_height

    pos_x = (screen_width - width) // 2
    pos_y = (screen_height - height) // 2
    win = curses.newwin(height, width, pos_y, pos_x)
    win.border()

    win.overlay(con)
    win.noutrefresh()
