from entity import Entity
from colors import color
import tileset
from game_states import GameStates
from rendering import RenderOrder


class Player(Entity):
    def __init__(self, combat, name='Player', blocks=True):
        super(Player, self).__init__(0, 0, tileset.PLAYER,
                                     color('WHITE_BOLD'), name,
                                     combat=combat,
                                     render_order=RenderOrder.ACTOR)
        self.fov_radius = 8

    @property
    def fov_radius(self):
        return self.__fov_radius

    @fov_radius.setter
    def fov_radius(self, val):
        self.__fov_radius = val

    def dead(self):
        # we don't call parents' dead() here
        # as we want the corpse's render_order to be identical to that of ACTOR
        # so that we can see the player's corpse
        self.rep = tileset.GRAVE

        return 'YOU ARE DEAD!!'
