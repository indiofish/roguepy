import curses
import textwrap
import msgbox
import string
import colors
from math import ceil
from utils import center_position


def menu(con, header, options, width, screen_width, screen_height, page):
    """ show a menu that uses single digits for hotkeys
    and this menu has pages """

    contents_per_page = 10  # use single digits for hotkeys

    header_wrapped = textwrap.wrap(header, width)
    header_height = len(header_wrapped)
    height = contents_per_page + 2 # +2 for border
    total_page = ceil(len(options) / contents_per_page)

    pos_x, pos_y = center_position(width, height, screen_width, screen_height)

    # Note: might change to subwin, relative to game screen
    win = curses.newwin(height, width, pos_y, pos_x)
    win.border()
    win.overlay(con)

    # display title
    for i, l in enumerate(header_wrapped):
        win.addstr(0, i+1, l)

    # display page number
    win.addstr(0, width-3-1, "{0}/{1}".format(page, total_page))

    # 0~9 for first page, 10~19 for second page...
    start_idx = (page-1) * contents_per_page
    for i, option in enumerate(options[start_idx: 
                                       start_idx+contents_per_page]):
        txt = '(' + str(i) + '): ' + str(option)
        win.addstr(i+1, 1, txt)

    win.noutrefresh()

def inventory_menu(con, inventory, width, 
                   screen_width, screen_height, page):

    items = [i for i in inventory.items] 
    menu(con, "INVENTORY", items, width, screen_width, screen_height, 1)



