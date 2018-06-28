import curses
import tdl
import input_handler
import rendering
import maps
from colors import color
import colors
from entity import Entity
# import locale


def main(stdscr):
    # locale.setlocale(locale.LC_ALL, '')
    # temporary constants
    room_max_size = 10
    room_min_size = 5
    max_rooms = 15

    height = 151
    width = 150
    win = curses.newpad(height, width)

    base_height, base_width = stdscr.getmaxyx()
    colors.init_colors()
    stdscr.bkgd(' ')
    stdscr.clear()
    stdscr.refresh()

    win.bkgd(' ')
    curses.curs_set(0)  # hide cursor

    map_height = 150
    map_width = 150
    game_map = maps.GameMap(map_width, map_height)

    player = Entity(0, 0, '@', color(colors.WHITE_BOLD))

    maps.generate_map(game_map, max_rooms, room_min_size, room_max_size,
                      map_width, map_height, player)

    entities = [player]

    # initial compute
    game_map.compute_fov(player.x, player.y)
    while True:
        rendering.render_all(win, entities, game_map, 70, 30, player.x,
                             player.y, base_width, base_height)
        action = input_handler.handle_input(win)
        mv = action.get('move')
        if mv:
            dx, dy = mv
            if game_map.walkable[player.x+dx, player.y+dy]:
                game_map.compute_fov(player.x, player.y)
                player.move(dx, dy)
            # else:
                # break


curses.wrapper(main)
