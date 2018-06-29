from entity import Entity
import colors
import tileset


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__(0, 0, tileset.PLAYER,
                                     colors.color(colors.WHITE_BOLD))
        self.fov_radius = 8

    @property
    def fov_radius(self):
        return self.__fov_radius

    @fov_radius.setter
    def fov_radius(self, val):
        self.__fov_radius = val
