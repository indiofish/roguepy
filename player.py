from entity import Entity
import colors
import tileset
from game_states import GameStates


class Player(Entity):
    def __init__(self, combat, name='Player', blocks=True):
        super(Player, self).__init__(0, 0, tileset.PLAYER,
                                     colors.color(colors.WHITE_BOLD), name,
                                     combat=combat)
        self.fov_radius = 8

    @property
    def fov_radius(self):
        return self.__fov_radius

    @fov_radius.setter
    def fov_radius(self, val):
        self.__fov_radius = val

    def dead(self):
        self.rep = tileset.GRAVE

        return 'YOU ARE DEAD!!'
