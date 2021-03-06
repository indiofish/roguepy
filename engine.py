import curses
# import tdl
import input_handler
import rendering
from rendering import RenderOrder
import maps
from colors import color, init_colors
from entity import Entity, blocking_entity_at_position
from player import Player
import tileset
from game_states import GameStates
from components.combat import Combat
from components.inventory import Inventory
from msgbox import MsgBox
from menus import Menu


def main(stdscr):
    # locale.setlocale(locale.LC_ALL, '')
    curses.nonl()

    # constants related to rooms
    room_max_size = 15
    room_min_size = 5
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
    # FIXME: as of now, we are going to assume that stdscr size doesn't change
    # stdscr is automatically init by wrapper()
    base_height, base_width = stdscr.getmaxyx()
    # constants related to view size
    # TODO: change view size in relation to screen size
    view_width = 100
    view_height = 24


    # default setups
    init_colors()
    curses.curs_set(0)  # hide cursor
    # win has to be a pad, so that scrolling is easily supported
    win = curses.newpad(height, width)
    win.keypad(True)
    win.bkgd(' ')
    # msgwin
    msg_win = curses.newpad(10, 100)
    msgbox = MsgBox(msg_win, view_width, view_height, base_width, base_height)

    # bars
    bar_width = 33
    bar_height = 1
    bar_win = curses.newwin(bar_height, bar_width, 1, 1)
    # bar_win.border()


    combat_module = Combat(hp=30, defense=2, power=5)
    inventory = Inventory(26)
    player = Player(combat_module, inventory)
    entities = [player]
    game_map = maps.GameMap(map_width, map_height)
    maps.generate_map(game_map, max_rooms, room_min_size,
                      room_max_size, player, entities)

    game_state = GameStates.PLAYERS_TURN
    previous_game_state = game_state
    # initial compute of fov
    game_map.compute_fov(player)
    inventory_menu = Menu(win, "INVENTORY", 30, base_width, base_height)
    while True:
        rendering.render_all(win, entities, game_map, view_width, view_height,
                             player, base_width, base_height, msgbox, bar_win,
                             inventory_menu, game_state)
        action = input_handler.handle_input(win, game_state)

        mv = action.get('move')
        pickup = action.get('pickup')
        show_inventory = action.get('show_inventory')
        hide_inventory = action.get('hide_inventory')
        item_at_cursor = action.get('item_at_cursor')
        inventory_index = action.get('inventory_index')
        move_cursor = action.get('move_cursor')
        move_page = action.get('move_page')
        exit = action.get('exit')
        
        inventory_shown = False

        player_turn_results = []

        if mv:
            dx, dy = mv
            dest_x = player.x + dx
            dest_y = player.y + dy

            if game_map.walkable[dest_x, dest_y]:
                target = blocking_entity_at_position(entities, dest_x, dest_y)
                if target:
                    atk_results = player.combat.attack(target)
                    player_turn_results.extend(atk_results)
                else:
                    move_results = {'move': mv}
                    player_turn_results.append(move_results)
        elif pickup:
            for e in entities:
                if e.item and e.x == player.x and e.y == player.y:
                    pickup_results = player.inventory.add_item(e)
                    player_turn_results.extend(pickup_results)
                    # only acquire one item at one turn 
                    break
            else:
                msgbox.add("no_item")
        # Toggle Inventory screen
        elif show_inventory:
            msgbox.add("open inven")
            previous_game_state = game_state
            game_state = GameStates.SHOW_INVENTORY
            # FIXME: cursor, page should have a value limit
            # and it probably should be handled by menus, not here
        elif exit:
            # quit game
            # break
            pass
        if GameStates.SHOW_INVENTORY:
            if move_cursor:
                inventory_menu.next_item(move_cursor)
            elif move_page:
                inventory_menu.next_page(move_page)
            elif hide_inventory:
                game_state = previous_game_state
            elif item_at_cursor:
                item = inventory_menu.item_at_cursor()
                if item:  # TEMP FIX: check validity of choice at menu?
                    use_results = player.inventory.use_item(item)
                    player_turn_results.extend(use_results)
            elif inventory_index is not None:
                # unlike other inputs, inventory_index can be 0,
                # so compare it with "None"
                # check will cause input 0 to be ignored
                item = inventory_menu.item_at(inventory_index)
                if item:
                    use_results = player.inventory.use_item(item)
                    player_turn_results.extend(use_results)

        # evaluate results of player turn
        for result in player_turn_results:
            movement = result.get('move')
            dead_entity = result.get('dead')
            item_added = result.get('item_added')
            msg = result.get('msg')
            item_used = result.get('item_used')
            if movement:
                dx, dy = movement
                player.move(dx, dy)
                game_map.compute_fov(player)
            if item_added:
                entities.remove(item_added)
            if msg:
                msgbox.add(msg)
            if dead_entity == player:
                game_state = GameStates.PLAYER_DEAD
            if item_used:
                inventory_shown = True


            # toggle state only when something is done in PLAYERS_TURN 
            game_state = GameStates.ENEMY_TURN

        if game_state == GameStates.ENEMY_TURN:
            # move those with ai modules
            enemies = (e for e in entities if e.ai)
            for e in enemies:

                e_turn_results = e.ai.take_turn(player, game_map, entities)

                # still a bit WET!
                for result in e_turn_results:
                    msg = result.get('msg')
                    dead_entity = result.get('dead')
                    if msg:
                        msgbox.add(msg)
                    if dead_entity == player:
                        game_state = GameStates.PLAYER_DEAD


        # check whether to return to beginning of loop
        if game_state == GameStates.PLAYER_DEAD:
            break
        elif game_state == GameStates.SHOW_INVENTORY:
            pass
        #if item was used at screen, keep the inventory opened
        elif inventory_shown:
            game_state = GameStates.SHOW_INVENTORY
        else:
            game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    curses.wrapper(main)
