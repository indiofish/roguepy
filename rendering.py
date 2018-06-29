from colors import color
import colors
import tileset


def render_all(win, entities, game_map, width, height, player_x, player_y,
               base_w, base_h):
    draw_map(win, game_map)
    for e in entities:
        draw_entity(win, e, game_map.fov)

    # map_height, map_width = game_map.height, game_map.width
    start_x = min(max(0, player_x - width // 2), game_map.width - width)
    start_y = min(max(0, player_y - height // 2), game_map.height - height)
    # stdscr.addstr(20, 100, "x:" + str(player_x), colors.COLOR_WHITE_BOLD)
    # stdscr.addstr(21, 100, "y:"+str(player_y), colors.COLOR_WHITE_BOLD)
    # stdscr.addstr(22, 100, "w:" + str(start_x), colors.COLOR_WHITE_BOLD)
    # stdscr.addstr(23, 100, "h:"+str(start_y), colors.COLOR_WHITE_BOLD)
    # stdscr.refresh()

    # calculate the start of the position it is displayed
    pos_x = (base_w - width) // 2
    pos_y = (base_h - height) // 2
    win.refresh(start_y, start_x, pos_y, pos_x, height+pos_y, width+pos_x)


def clear_all(win, entities):
    for e in entities:
        clear_entity(win, e)


def draw_entity(win, entity, fov):
    if fov[entity.x, entity.y]:
        win.addstr(entity.y, entity.x, entity.rep, entity.color)


def clear_entity(win, entity):
    win.addch(entity.y, entity.x, ' ', color(colors.BLACK))


def draw_map(win, game_map):
    for x, y in game_map:
        wall = not game_map.transparent[x, y]
        if game_map.fov[x, y]:
            # if in fov then explored
            game_map.explored[x][y] = True
            if wall:
                win.addch(y, x, tileset.WALL, color(colors.LIGHT_GRAY))
            else:
                win.addch(y, x, tileset.FLOOR, color(colors.LIGHT_GRAY))
        elif game_map.explored[x][y]:
            if wall:
                win.addch(y, x, tileset.WALL, color(colors.DARK_GRAY))
            else:
                win.addch(y, x, tileset.FLOOR, color(colors.DARK_GRAY))
