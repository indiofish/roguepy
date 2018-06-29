from tdl.map import Map
from random import randint


class GameMap(Map):
    def __init__(self, width, height):
        super(GameMap, self).__init__(width, height)
        self.explored = [[False for y in range(height)] for x in range(width)]

    def compute_fov(self, player, fov='DIAMOND', light_walls=True):
        """simple override for simpler function usage"""
        return super(GameMap, self).compute_fov(player.x, player.y,
                                                fov=fov,
                                                radius=player.view_radius,
                                                light_walls=light_walls)


class Rect:
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


def generate_map(game_map, max_rooms, room_min_size, room_max_size, map_width,
                 map_height, player):

    rooms = []
    rooms_count = 0

    for r in range(max_rooms):
        w = randint(room_min_size, room_max_size)
        h = randint(room_min_size, room_max_size)

        x = randint(0, map_width - w - 1)
        y = randint(0, map_height - h - 1)

        new_room = Rect(x, y, w, h)

        # TODO: fix this code
        if rooms_count == 0:  # if this is a new room
            player.x, player.y = new_room.center()
            create_room(game_map, new_room)
            rooms.append(new_room)
            rooms_count += 1
        else:
            for other_rooms in rooms:
                if new_room.intersect(other_rooms):
                    break
                else:
                    create_room(game_map, new_room)
                    new_x, new_y = new_room.center()
                    (prev_x, prev_y) = rooms[rooms_count-1].center()
                    if randint(0, 1):
                        create_h_tunnel(game_map, prev_x, new_x, prev_y)
                        create_v_tunnel(game_map, prev_y, new_y, new_x)
                    else:
                        create_v_tunnel(game_map, prev_y, new_y, prev_x)
                        create_h_tunnel(game_map, prev_x, new_x, new_y)

                    rooms.append(new_room)
                    rooms_count += 1
