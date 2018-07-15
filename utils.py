def center_position(width, height, main_width, main_height):
    """The leftcorner of a window that needs to be centered relative to the
    main screen"""
    pos_x = (main_width - width) // 2
    pos_y = (main_height - height) // 2

    return (pos_x, pos_y)
