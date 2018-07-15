import curses


def handle_input(win):
    user_input = win.getkey()
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
