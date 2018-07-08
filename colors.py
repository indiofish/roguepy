import curses

# COLOR_BKGD = -1
WHITE = 0
BLACK = 1
RED = 2
GREEN = 3
YELLOW = 4
BLUE = 5
MAGENTA = 6
CYAN = 7
GRAY = 8
RED_BOLD = 10
GREEN_BOLD = 11
YELLOW_BOLD = 12
BLUE_BOLD = 13
MAGENTA_BOLD = 14
CYAN_BOLD = 15
WHITE_BOLD = 16
DARK_GRAY = 237
LIGHT_GRAY = 241
DARK_RED = 89
RED_BKGD = 90


def init_colors():
    curses.use_default_colors()
    for i in range(curses.COLORS):
        curses.init_pair(i+1, i, -1)

    curses.init_pair(90, 2, 1)


def color(i):
    return curses.color_pair(i)
