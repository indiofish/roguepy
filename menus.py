import curses
import textwrap
import msgbox
import string
import colors
from math import ceil
from utils import center_position


def menu(con, header, options, width, screen_width, screen_height, 
         cursor, page):
    """ show a menu that uses single digits for hotkeys
    and this menu has pages """

    contents_per_page = 10  # use single digits for hotkeys

    header_wrapped = textwrap.wrap(header, width)
    header_height = len(header_wrapped)
    height = contents_per_page + 2 # +2 for border

    # max(1, X) for cases where there are no items
    # total_page will still be 1
    total_page = max(1, ceil(len(options) / contents_per_page))

    pos_x, pos_y = center_position(width, height, screen_width, screen_height)

    # Note: might change to subwin, relative to game screen
    # +5 for text window
    win = curses.newwin(height+5, width, pos_y, pos_x)
    txt_win = win.subwin(pos_y+height, pos_x)

    txt_win.border()
    win.border()
    win.overlay(con)

    cursor = cursor % min(len(options), contents_per_page)
    page = (page % total_page) + 1

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

        if cursor == i:
            win.addstr(i+1, 1, txt, curses.A_REVERSE)
            if hasattr(option, 'flavor_text'):
                txt_win.addstr(1, 1, option.flavor_text)
        else:
            win.addstr(i+1, 1, txt)

    win.noutrefresh()

def inventory_menu(con, inventory, width, 
                   screen_width, screen_height, 
                   cursor, page):

    items = [i for i in inventory.items] 
    menu(con, "INVENTORY", items, width, screen_width, screen_height, cursor,
         page)
