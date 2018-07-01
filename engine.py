import curses
# import tdl
import input_handler
import rendering
import maps
from colors import color
import colors
from entity import Entity
from player import Player
import tileset
from debug import log
# import locale


def main(stdscr):
    # locale.setlocale(locale.LC_ALL, '')

    # constants related to rooms
    room_max_size = 20
    room_min_size = 10
    max_rooms = 15

    # constants related to padding size
    # either height/width has to be larger than their counterparts of map
    # becuase writing on the bottom right corner of the padding causes an error
    height = 151
    width = 150
    # constants related to map size
    map_height = 150
    map_width = 150
    # get size of the screen for positioning
    base_height, base_width = stdscr.getmaxyx()
    # constants related to view size
    # TODO: change view size in relation to screen size
    view_width = 70
    view_height = 24

    # stdscr is automatically init by wrapper()
    stdscr.bkgd(' ')

    # win has to be a pad, so that scrolling is easily supported
    win = curses.newpad(height, width)
    win.bkgd(' ')

    colors.init_colors()
    curses.curs_set(0)  # hide cursor

    # debugging console
    log.scr = stdscr
    log(1)
    player = Player()
    entities = [player]
    game_map = maps.GameMap(map_width, map_height)
    maps.generate_map(game_map, max_rooms, room_min_size,
                      room_max_size, player, entities)

    # initial compute of fov
    game_map.compute_fov(player)
    while True:
        rendering.render_all(win, entities, game_map, view_width, view_height,
                             player.x, player.y, base_width, base_height)
        action = input_handler.handle_input(win)
        mv = action.get('move')
        if mv:
            dx, dy = mv
            if game_map.walkable[player.x+dx, player.y+dy]:
                game_map.compute_fov(player)
                player.move(dx, dy)
            # else:
                # break


curses.wrapper(main)
