import curses
import colors

def render_all(win, entities, game_map, width, height, player_x, player_y,
               fov_recompute):
    draw_map(win, game_map, fov_recompute)
    for e in entities:
        draw_entity(win, e)

    # map_height, map_width = game_map.height, game_map.width
    start_x = min(max(0, player_x - width // 2), game_map.width - width)
    start_y = min(max(0, player_y - height // 2), game_map.height - height)
    # stdscr.addstr(20, 100, "x:" + str(player_x), colors.COLOR_WHITE_BOLD)
    # stdscr.addstr(21, 100, "y:"+str(player_y), colors.COLOR_WHITE_BOLD)
    # stdscr.addstr(22, 100, "w:" + str(start_x), colors.COLOR_WHITE_BOLD)
    # stdscr.addstr(23, 100, "h:"+str(start_y), colors.COLOR_WHITE_BOLD)
    # stdscr.refresh()
    win.refresh(start_y, start_x, 0, 0, height, width)

def clear_all(win, entities):
    for e in entities:
        clear_entity(win, e)

def draw_entity(win, entity):
    win.addch(entity.y, entity.x, entity.rep, entity.color)

def clear_entity(win, entity):
    win.addch(entity.y, entity.x, ' ', curses.color_pair(1))

def draw_map(win, game_map, fov_recompute):
    for x, y in game_map:
        wall = not game_map.transparent[x, y]
        if game_map.fov[x, y]:
            if wall:
                win.addch(y, x, '#', colors.COLOR_LIGHT_GRAY)
            else:
                win.addch(y, x, '.', colors.COLOR_GRAY)
        else:
            if wall:
                win.addch(y, x, '#', colors.COLOR_BLACK)
            else:
                win.addch(y, x, '.', colors.COLOR_BLACK)
