from game_states import GameStates
import tileset
import colors

def kill_player(player):
    player.char = tileset.GRAVE

    return 'DEAD!!', GameStates.PLAYER_DEAD

def kill_mob(mob):
    death_msg = '{0} is dead!'.format(mob.name)

    mob.char = tileset.CORPSE
    mob.color = colors.color(colors.RED)
    mob.blocks = False
    mob.combat = None
    mob.ai = None
    mob.name = 'remains of {0}'.format(mob.name)

    return death_msg
