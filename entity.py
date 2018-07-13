import math
from rendering import RenderOrder


class Entity():
    """Top level generic object for allmost anything"""
    def __init__(self, x, y, rep, color, name,
                 render_order=RenderOrder.CORPSE, 
                 blocks=False, combat=None, ai=None,
                 item=None, inventory=None):
        self.x = x
        self.y = y
        self.rep = rep  # character that represents this
        self.name = name
        self.color = color
        self.blocks = blocks
        self.combat = combat
        self.ai = ai
        self.render_order = render_order
        self.item = item
        self.inventory = inventory

        if self.combat:
            self.combat.owner = self
        if self.ai:
            self.ai.owner = self
        if self.item:
            self.item.owner = self
        if self.inventory:
            self.inventory.owner = self

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_towards(self, target_x, target_y, game_map, entities):
        path = game_map.compute_path(self.x, self.y, target_x, target_y)

        dx = path[0][0] - self.x
        dy = path[0][1] - self.y

        if (game_map.walkable[path[0][0], path[0][1]] and
            not blocking_entity_at_position(entities, path[0][0], path[0][1])):
            self.move(dx, dy)

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return math.sqrt(dx**2 + dy**2)

    def dead(self):
        self.render_order = RenderOrder.CORPSE


def blocking_entity_at_position(entities, pos_x, pos_y):

    # ugly but lets keep it this way for a while
    for e in entities:
        if e.blocks:
            if pos_x == e.x and pos_y == e.y:
                return e

    return None
