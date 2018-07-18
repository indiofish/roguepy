from colors import color
import tileset
from enum import Enum
from game_states import GameStates
from curses import doupdate
from utils import center_position
from menus import Menu
import curses

class RenderOrder(Enum):
    CORPSE = 1
    ITEM = 2
    ACTOR = 3



def render_all(win, entities, game_map, width, height, player,
               base_w, base_h, msgbox, panel, inventory_menu,
               game_state):

    draw_map(win, game_map)

    entities_in_render_order = sorted(entities, 
                                      key=lambda x: x.render_order.value)
    for e in entities_in_render_order:
        draw_entity(win, e, game_map.fov)


    player_x, player_y = player.x, player.y

    start_x, start_y = view_position(game_map.width, game_map.height,
                                     width, height, player_x, player_y)
    pos_x, pos_y = center_position(width, height, base_w, base_h)
    render_bar(panel, player.combat.hp, player.combat.max_hp, 'HP')
    win.noutrefresh(start_y, start_x, pos_y, pos_x, height+pos_y, width+pos_x)
    msgbox.print()

    if game_state == GameStates.SHOW_INVENTORY:
        inventory_menu.display(player.inventory.items)
    doupdate()




def view_position(game_map_w, game_map_h, width, height, player_x, player_y):
    """The top left corner of the area player can view, with @ at the center"""
    start_x = min(max(0, player_x - width // 2), game_map_w - width)
    start_y = min(max(0, player_y - height // 2), game_map_h - height)

    return (start_x, start_y)


def render_bar(panel, value, maximum, name):
    #TODO: remove magic numbers & clean up
    _, total_width = panel.getmaxyx()
    panel.erase()

    panel.addstr(0, 0, name, color('RED'))
    panel.addstr(0, len(name), '[', color('RED'))
    panel.addstr(0, total_width-2, ']', color('RED'))

    total_width -= (3 + len(name))

    bar_width = int(float(value) / maximum * total_width)

    if bar_width > 0:
        panel.addstr(0, len(name)+1, '#' * bar_width,
                     color('RED'))

    panel.noutrefresh()



def clear_all(win, entities):
    for e in entities:
        clear_entity(win, e)


def draw_entity(win, entity, fov):
    if fov[entity.x, entity.y]:
        win.addstr(entity.y, entity.x, entity.rep, entity.color)


def clear_entity(win, entity):
    win.addch(entity.y, entity.x, ' ', color('BLACK'))


def draw_map(win, game_map):
    for x, y in game_map:
        wall = not game_map.transparent[x, y]
        if game_map.fov[x, y]:
            # if in fov then explored
            game_map.explored[x][y] = True
            if wall:
                win.addch(y, x, tileset.WALL, color('LIGHT_GRAY'))
            else:
                win.addch(y, x, tileset.FLOOR, color('LIGHT_GRAY'))
            if game_map.doors.get((x, y)) == 'h':
                win.addch(y, x, tileset.H_DOOR, color('BROWN'))
            elif game_map.doors.get((x, y)) == 'v':
                win.addch(y, x, tileset.V_DOOR, color('BROWN'))

        elif game_map.explored[x][y]:
            if wall:
                win.addch(y, x, tileset.WALL, color('DARK_GRAY'))
            else:
                win.addch(y, x, tileset.FLOOR, color('DARK_GRAY'))
            if game_map.doors.get((x, y)) == 'h':
                win.addch(y, x, tileset.H_DOOR, color('BROWN'))
            elif game_map.doors.get((x, y)) == 'v':
                win.addch(y, x, tileset.V_DOOR, color('BROWN'))

        else:
            win.addch(y, x, '#', color('DARKER_GRAY'))
