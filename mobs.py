from entity import Entity
from colors import color
import tileset
from rendering import RenderOrder


class Mob(Entity):
    def __init__(self, x, y, char, combat, ai, blocks=True):
        super(Mob, self).__init__(x, y, u'\u04e7',
                                  color('GREEN'),
                                  'mob', blocks=blocks, combat=combat, ai=ai,
                                  render_order=RenderOrder.ACTOR)
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

    def dead(self):
        super().dead()
        death_msg = '{0} is dead!'.format(self.name)

        self.rep = tileset.CORPSE
        self.color = color('DARK_RED')
        self.blocks = False
        self.combat = None
        self.ai = None
        self.name = 'remains of {0}'.format(self.name)

        return death_msg
