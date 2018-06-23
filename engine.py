import curses
import input_handler
import rendering
from entity import Entity


def main(stdscr):
    base_height, base_width = stdscr.getmaxyx()
    height = 30
    width = 60
    begin_x = base_width//2 - width//2
    begin_y = base_height//2 - height//2

    # TODO: move to colors.py
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)

    win = curses.newwin(height, width, begin_y, begin_x)
    stdscr.bkgd(' ',curses.color_pair(-1))
    stdscr.refresh()
    win.bkgd(' ', curses.color_pair(1))
    win.refresh()

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    player = Entity(width//2, height//2, '@', curses.color_pair(2))
    entities = [player]
    curses.curs_set(0)  # hide cursor
    rendering.render_all(win, entities, 0, 0)
    curses.doupdate()  # TODO: move this to rendering.py?

    while True:
        action = input_handler.handle_input(win)
        rendering.clear_entity(win, player)
        mv = action.get('move')
        if mv:
            dx, dy = mv
            player.move(dx, dy)
        else:
            break
        rendering.draw_entity(win, player)
    win.refresh()


curses.wrapper(main)
