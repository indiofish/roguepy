import colors

pos_x = 10
pos_y = 5


def log(text):
    global pos_x, pos_y
    log.scr.addstr(pos_y, pos_x, text,
                   colors.color(colors.WHITE_BOLD))
    pos_y += 1
    log.scr.refresh()
