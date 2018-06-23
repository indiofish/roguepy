def handle_input(win):
    user_input = win.getkey()
    # Movement keys
    if user_input == 'k':
        return {'move': (0, -1)}
    elif user_input == 'j':
        return {'move': (0, 1)}
    elif user_input == 'h':
        return {'move': (-1, 0)}
    elif user_input == 'l':
        return {'move': (1, 0)}
    else:
        return {'exit': True}

    # No user_input was pressed
    return {}
