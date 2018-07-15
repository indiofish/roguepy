import curses
from game_states import GameStates


def handle_input(win, game_state):
    user_input = win.getkey()
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_input(user_input)
    elif game_state == GameStates.PLAYER_DEAD:
        pass
    elif game_state == GameStates.SHOW_INVENTORY:
        return handle_inventory_input(user_input)
    else:
        return {}


def handle_inventory_input(user_input):
    if user_input == 'i':
        return {'hide_inventory': True}
    elif user_input in '0123456789':
        return {'inventory_index': int(user_input)}
    elif user_input in ('\n', '\r', 'KEY_ENTER'):
        return {'item_at_cursor': True}
    elif user_input == 'k' or user_input == 'KEY_UP':
        return {'move_cursor': -1}
    elif user_input == 'j' or user_input == 'KEY_DOWN':
        return {'move_cursor': 1}
    elif user_input == 'h' or user_input == 'KEY_LEFT':
        return {'move_page': -1}
    elif user_input == 'l' or user_input == 'KEY_RIGHT':
        return {'move_page': 1}
    else:
        return {}

def handle_player_turn_input(user_input):
    # Movement keys
    if user_input == 'k' or user_input == 'KEY_UP':
        return {'move': (0, -1)}
    elif user_input == 'j' or user_input == 'KEY_DOWN':
        return {'move': (0, 1)}
    elif user_input == 'h' or user_input == 'KEY_LEFT':
        return {'move': (-1, 0)}
    elif user_input == 'l' or user_input == 'KEY_RIGHT':
        return {'move': (1, 0)}
    elif user_input == 'y':
        return {'move': (-1, -1)}
    elif user_input == 'u':
        return {'move': (1, -1)}
    elif user_input == 'b':
        return {'move': (-1, 1)}
    elif user_input == 'n':
        return {'move': (1, 1)}
    elif user_input == 'g':
        return {'pickup': True}
    elif user_input == 'i':
        return {'show_inventory': True}
    elif user_input =='q':
        return {'exit': True}
    else:
        return {'exit': True}

    # No user_input was pressed
    return {}
