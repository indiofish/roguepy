from entity import Entity
import colors
import tileset


class Mob(Entity):
    def __init__(self, x, y, char):
        super(Mob, self).__init__(x, y, 'd', colors.color(colors.GREEN))
        # eyesight
        self.fov_radius = 8
        # hitpoints
        self.hp = 0
        # mana
        self.mp = 0

    @property
    def fov_radius(self):
        return self.__fov_radius

    @fov_radius.setter
    def fov_radius(self, val):
        self.__fov_radius = val
