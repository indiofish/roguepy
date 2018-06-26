import curses

COLOR_BKGD = 0
COLOR_WHITE = 0
COLOR_BLACK = 0
COLOR_RED = 0
COLOR_GREEN =0
COLOR_YELLOW = 0
COLOR_BLUE = 0
COLOR_MAGENTA = 0
COLOR_CYAN = 0
COLOR_GRAY = 0
COLOR_RED_BOLD = 0
COLOR_GREEN_BOLD = 0
COLOR_YELLOW_BOLD = 0
COLOR_BLUE_BOLD = 0
COLOR_MAGENTA_BOLD = 0
COLOR_CYAN_BOLD = 0
COLOR_WHITE_BOLD = 0
COLOR_DARK_GRAY = 0
COLOR_LIGHT_GRAY = 0


def init_colors():
    global COLOR_BKGD
    global COLOR_WHITE
    global COLOR_BLACK
    global COLOR_RED
    global COLOR_GREEN
    global COLOR_YELLOW
    global COLOR_BLUE
    global COLOR_MAGENTA
    global COLOR_CYAN
    global COLOR_GRAY
    global COLOR_RED_BOLD
    global COLOR_GREEN_BOLD
    global COLOR_YELLOW_BOLD
    global COLOR_BLUE_BOLD
    global COLOR_MAGENTA_BOLD
    global COLOR_CYAN_BOLD
    global COLOR_WHITE_BOLD
    global COLOR_DARK_GRAY
    global COLOR_LIGHT_GRAY

    curses.use_default_colors()
    for i in range(curses.COLORS):
        curses.init_pair(i+1, i, -1)

    COLOR_BKGD = curses.color_pair(-1)
    COLOR_WHITE = curses.color_pair(0)
    COLOR_BLACK = curses.color_pair(1)
    COLOR_RED = curses.color_pair(2)
    COLOR_GREEN = curses.color_pair(3)
    COLOR_YELLOW = curses.color_pair(4)
    COLOR_BLUE = curses.color_pair(5)
    COLOR_MAGENTA = curses.color_pair(6)
    COLOR_CYAN = curses.color_pair(7)
    # curses.init_pair(8, 7, 240)
    COLOR_GRAY = curses.color_pair(8)
    COLOR_RED_BOLD = curses.color_pair(10)
    COLOR_GREEN_BOLD = curses.color_pair(11)
    COLOR_YELLOW_BOLD = curses.color_pair(12)
    COLOR_BLUE_BOLD = curses.color_pair(13)
    COLOR_MAGENTA_BOLD = curses.color_pair(14)
    COLOR_CYAN_BOLD = curses.color_pair(15)
    COLOR_WHITE_BOLD = curses.color_pair(16)
    COLOR_DARK_GRAY = curses.color_pair(237)
    COLOR_LIGHT_GRAY = curses.color_pair(241)
