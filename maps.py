from tdl.map import Map
from random import randint
from mobs import Mob
from debug import log
from components.combat import Combat
from components.ai import BasicMonster


class GameMap(Map):
    def __init__(self, width, height):
        super(GameMap, self).__init__(width, height)
        self.explored = [[False for y in range(height)] for x in range(width)]

    def compute_fov(self, player, fov='PERMISSIVE', light_walls=True):
        """simple override for simpler function usage"""
        return super(GameMap, self).compute_fov(player.x, player.y,
                                                fov=fov,
                                                radius=player.fov_radius,
                                                light_walls=light_walls)


class Rect():
    def __init__(self, x, y, w, h):

        # x1, y1 : left corner
        self.x1 = x
        self.x2 = x+w
        self.y1 = y
        self.y2 = y+h

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


def create_room(game_map, room):
    # go through the tiles in the rectangle and make them passable

    # +1 for wall paddings
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            game_map.walkable[x, y] = True
            game_map.transparent[x, y] = True


def generate_map(game_map, max_rooms, room_min_size, room_max_size, player,
                 entities):

    rooms = generate_rooms(game_map, max_rooms, room_min_size, room_max_size)
    for r in rooms:
        create_room(game_map, r)
    generate_tunnels(game_map, rooms)

    mobs = generate_mobs(rooms[1:], 3)

    entities += mobs

    # place the player in the first room made
    player.x, player.y = rooms[0].center()


def generate_mobs(rooms, max_mobs_per_room):
    """fill in the rooms with mobs"""
    # how do we ensure that no mobs are on the same position?
    # we create a temporary dictionary of mobs with position as key
    mobs = {}

    # TODO: we will pick mobs from available mobs list
    for room in rooms:
        n_of_mobs = randint(0, max_mobs_per_room)
        for i in range(n_of_mobs):
            # +-1 since we cannot place mobs in walls
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            combat_module = Combat(10, 0, 5)
            ai_module = BasicMonster()
            mobs[x, y] = Mob(x, y, 'd', combat_module, ai_module)

    # extract mob(values) from mobs(dict)
    return list(mobs.values())


def generate_rooms(game_map, max_rooms, room_min_size, room_max_size):
    rooms = []

    for r in range(max_rooms):
        w = randint(room_min_size, room_max_size)
        h = randint(room_min_size, room_max_size)

        x = randint(0, game_map.width - w - 1)
        y = randint(0, game_map.height - h - 1)

        new_room = Rect(x, y, w, h)

        if not rooms:  # if this is a new room
            # this ensures that the first room the player is in
            # is first room in [rooms]
            rooms.append(new_room)
        else:  # if we have rooms
            # if other rooms do not intersect with new ones
            if sum(1 for r in rooms if new_room.intersect(r)) == 0:
                rooms.append(new_room)

    return rooms


def create_h_tunnel(game_map, x1, x2, y, width=1):
    for x in range(min(x1, x2), max(x1, x2)+1):
        for w in range(width):
            game_map.walkable[x, y+w] = True
            game_map.transparent[x, y+w] = True


def create_v_tunnel(game_map, y1, y2, x, width=1):
    for y in range(min(y1, y2), max(y1, y2)+1):
        for w in range(width):
            game_map.walkable[x+w, y] = True
            game_map.transparent[x+w, y] = True


def generate_tunnels(game_map, rooms):
    """create tunnels that connect between two random rooms"""
    # init: get the first room as prev, and start from index 1
    prev_room = rooms[0]
    for r in rooms[1:]:
        new_x, new_y = r.center()
        prev_x, prev_y = prev_room.center()
        if randint(0, 1):
            create_h_tunnel(game_map, prev_x, new_x, prev_y)
            create_v_tunnel(game_map, prev_y, new_y, new_x)
        else:
            create_v_tunnel(game_map, prev_y, new_y, prev_x)
            create_h_tunnel(game_map, prev_x, new_x, new_y)

        prev_room = r
