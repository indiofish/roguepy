import curses
import textwrap
import msgbox
import string
import colors
from math import ceil
from utils import center_position


class Menu():
    """ show a menu that uses single digits for hotkeys
    and this menu has pages """
    def __init__(self, con, title, width, screen_width, screen_height):

        # use single digits for hotkeys
        self.contents_per_page = 10
        self.cursor = 0
        self.page = 0

        self.title_wrapped = textwrap.wrap(title, width)
        self.title_height = len(self.title_wrapped)
        self.width = width
        self.height = self.contents_per_page + 1 # +1 for border
        pos_x, pos_y = center_position(width, self.height, screen_width, screen_height)

        self.win = curses.newwin(self.height+5,width,pos_y,pos_x)
        self.txt_win = self.win.subwin(pos_y+self.height, pos_x)


        self.cursor = 0
        self.page = 0
        self.options = []
        self.total_page = 1

    def display(self, options):
        self.win.erase()
        self.txt_win.border()
        self.win.border()


        for i, l in enumerate(self.title_wrapped):
            self.win.addstr(0, i+1, l)
        self.options = options
        self.total_page = max(1, ceil(len(self.options) / self.contents_per_page))

        # display page number
        self.win.addstr(0, self.width-3-1,
                        "{0}/{1}".format(self.page+1, self.total_page))

        # 0~9 for first page, 10~19 for second page...
        start_idx = self.page * self.contents_per_page


        for i, option in enumerate(self.options[start_idx: 
                                                start_idx+self.contents_per_page]):
            txt = '(' + str(i) + '): ' + str(option)

            #FIXME: clean up screen for remaining characters
            if self.cursor == i:
                self.win.addstr(i+1, 1, txt, curses.A_REVERSE)
                if hasattr(option, 'flavor_text'):
                    self.txt_win.addstr(1, 1, option.flavor_text)
            else:
                self.win.addstr(i+1, 1, txt)

        self.win.noutrefresh()

    def hide():
        pass

    def next_item(self, idx):
        #cursor only moves when there is a item in menu
        if self.options:
            self.cursor += idx
            self.cursor = self.cursor % min(len(self.options), self.contents_per_page)

    def next_page(self, idx):
        self.page += idx
        self.page = self.page % self.total_page
