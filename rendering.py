import curses

def render_all(win, entities, width, height):
    for e in entities:
        draw_entity(win, e)

    # width and height will be used when we go to pad
    win.noutrefresh()

def clear_all(win, entities):
    for e in entities:
        clear_entity(win, e)

def draw_entity(win, entity):
    win.addch(entity.y, entity.x, entity.rep, entity.color)

def clear_entity(win, entity):
    win.addch(entity.y, entity.x, ' ', curses.color_pair(1))
