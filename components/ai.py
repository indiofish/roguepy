from debug import log
import math


class BasicMonster():
    """Basic AI for mobs"""
    def take_turn(self, target, game_map, entities):
        mob = self.owner

        # as of now, i see you you see me
        if game_map.fov[mob.x, mob.y]:
            if mob.distance_to(target) >= 2:
                mob.move_towards(target.x, target.y, game_map, entities)
                return "MOVE!"
            elif target.combat.hp > 0:
                return "ATTACK!"
        # log(self.owner.name)

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
