class Entity():
    """Top level generic object for allmost anything"""
    def __init__(self, x, y, rep, color, name, blocks=False):
        self.x = x
        self.y = y
        self.rep = rep  # character that represents this
        self.name = name
        self.color = color
        self.blocks = blocks

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def blocking_entity_at_position(entities, pos_x, pos_y):

    # ugly but lets keep it this way for a while
    for e in entities:
        if e.blocks:
            if pos_x == e.x and pos_y == e.y:
                return e

    return None
