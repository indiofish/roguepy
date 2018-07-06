import curses
# import tdl
import input_handler
import rendering
import maps
from colors import color
import colors
from entity import Entity, blocking_entity_at_position
from player import Player
import tileset
from game_states import GameStates
from components.combat import Combat
from msgbox import MsgBox
# import locale


def main(stdscr):
    # locale.setlocale(locale.LC_ALL, '')

    # constants related to rooms
    room_max_size = 20
    room_min_size = 10
    max_rooms = 30

    # constants related to padding size
    # either height/width has to be larger than their counterparts of map
    # becuase writing on the bottom right corner of the padding causes an error
    height = 151
    width = 150
    # constants related to map size
    map_height = 150
    map_width = 150
    # get size of the screen for positioning
    # FIXME: as of now, we are going to assume that stdscr size doesn't change
    base_height, base_width = stdscr.getmaxyx()
    # constants related to view size
    # TODO: change view size in relation to screen size
    view_width = 80
    view_height = 24

    # stdscr is automatically init by wrapper()
    stdscr.bkgd(' ')

    # win has to be a pad, so that scrolling is easily supported
    win = curses.newpad(height, width)
    msg_win = curses.newpad(10, 80)
    # msg_board = curses.newpad(20, 80)
    msgbox = MsgBox(msg_win, view_width, view_height, base_width, base_height)
    win.bkgd(' ')
    # msg_board.bkgd(' ')
    colors.init_colors()
    # log.scr = msg_board
    # log("HI")
    msgbox.refresh()

    curses.curs_set(0)  # hide cursor

    combat_module = Combat(hp=30, defense=2, power=5)
    player = Player(combat_module)
    entities = [player]
    game_map = maps.GameMap(map_width, map_height)
    maps.generate_map(game_map, max_rooms, room_min_size,
                      room_max_size, player, entities)

    game_state = GameStates.PLAYERS_TURN
    # initial compute of fov
    game_map.compute_fov(player)
    while True:
        rendering.render_all(win, entities, game_map, view_width, view_height,
                             player.x, player.y, base_width, base_height)
        action = input_handler.handle_input(win)
        mv = action.get('move')

        player_turn_results = []

        if mv and game_state == GameStates.PLAYERS_TURN:
            dx, dy = mv
            dest_x = player.x + dx
            dest_y = player.y + dy
            if game_map.walkable[player.x+dx, player.y+dy]:
                target = blocking_entity_at_position(entities, dest_x, dest_y)
                if target:
                    ret = player.combat.attack(target)
                    player_turn_results.extend(ret)
                else:
                    game_map.compute_fov(player)
                    player.move(dx, dy)
                    msgbox.print("move")

            game_state = GameStates.ENEMY_TURN

            for result in player_turn_results:
                msg = result.get('msg')
                dead_entity = result.get('dead')
                if msg:
                    msgbox.print(msg)
                if dead_entity:
                    # do sth
                    pass

        if game_state == GameStates.ENEMY_TURN:
            for e in entities:
                if e.ai:  # if it has an ai module
                    ret = e.ai.take_turn(player, game_map, entities)

                    for result in ret:
                        msg = result.get('msg')
                        dead_entity = result.get('dead')

                        if msg:
                            msgbox.print(msg)
                        if dead_entity:
                            pass # do something
            else:
                game_state = GameStates.PLAYERS_TURN


curses.wrapper(main)
