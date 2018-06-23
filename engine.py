import curses
import input_handler


def main(stdscr):
    base_height, base_width = stdscr.getmaxyx()
    height = 30
    width = 60
    begin_x = base_width//2 - width//2
    begin_y = base_height//2 - height//2

    # TODO: move to colors.py
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)

    win = curses.newwin(height, width, begin_y, begin_x)
    win.bkgd(' ', curses.color_pair(1))

    curr_pos = {'x': width//2, 'y': height//2}
    curses.curs_set(0)  # hide cursor
    curses.init_pair(35, curses.COLOR_RED, curses.COLOR_WHITE)
    win.addstr(curr_pos['y'], curr_pos['x'], "@", curses.color_pair(35))
    win.refresh()

    while True:
        action = input_handler.handle_input(win)
        win.delch(curr_pos['y'], curr_pos['x'])
        mv = action.get('move')
        if mv:
            dx, dy = mv
            curr_pos['x'] += dx
            curr_pos['y'] += dy
        else:
            break
        win.addstr(curr_pos['y'], curr_pos['x'], "@", curses.color_pair(35))
    win.refresh()


curses.wrapper(main)
