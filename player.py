from entity import Entity
import colors
import tileset


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__(0, 0, tileset.PLAYER,
                                     colors.color(colors.WHITE_BOLD))
