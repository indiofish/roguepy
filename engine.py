import curses
import tdl
import input_handler
import rendering
import maps
import colors
from entity import Entity


def main(stdscr):
    # temporary constants
    room_max_size = 10
    room_min_size = 5
    max_rooms = 10
    # base_height, base_width = stdscr.getmaxyx()
    # TODO: get these values based on base_height/weight
    height = 151
    width = 150
    win = curses.newpad(height, width)

    colors.init_colors()
    stdscr.bkgd(' ', colors.COLOR_BLACK)
    stdscr.clear()
    stdscr.refresh()

    win.bkgd(' ', colors.COLOR_BLACK)
    curses.curs_set(0)  # hide cursor

    map_height = 100
    map_width = 100
    game_map = tdl.map.Map(map_width, map_height)

    player = Entity(0, 0, '@', colors.COLOR_WHITE_BOLD)

    maps.generate_map(game_map, max_rooms, room_min_size, room_max_size,
                      map_width, map_height, player)

    entities = [player]

    while True:
        rendering.render_all(win, entities, game_map, 60, 20, player.x,
                             player.y, stdscr)
        action = input_handler.handle_input(win)
        mv = action.get('move')
        if mv:
            dx, dy = mv
            if game_map.walkable[player.x+dx, player.y+dy]:
                player.move(dx, dy)
        else:
            break


curses.wrapper(main)
