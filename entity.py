class Entity:
    """Top level generic object for allmost anything"""
    def __init__(self, x, y, rep, color):
        self.x = x
        self.y = y
        self.rep = rep  # character that represents this
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
