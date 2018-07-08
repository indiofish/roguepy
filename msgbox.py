# import colors
from rendering import main_window_position


class MsgBox():
    def __init__(self, win, main_w, main_h, base_w, base_h):
        self.win = win
        self.main_w = main_w
        self.main_h = main_h
        self.base_w = base_w
        self.base_h = base_h
        self.max_history = 100
        self.lines = [0] * self.max_history
        # -2 for borders top/bottom
        win_h, win_w = self.win.getmaxyx()
        self.max_lines = win_h - 2
        self.max_width = win_w - 2
        self.position = 0

        self.win.border()

    def refresh(self):
        pos_x, pos_y = main_window_position(self.main_w, self.main_h,
                                            self.base_w, self.base_h)
        y = self.main_h + pos_y
        win_h, win_w = self.win.getmaxyx()

        self.win.noutrefresh(0, 0, y+1, pos_x,
                         y+1+win_h, pos_x+win_w)

    def add(self, asset, color=0):
        self.lines[self.position] = str(asset)
        self.position = (self.position + 1) % self.max_history

    def print(self):
        i = 1
        for j in range(self.position-8, self.position):
            line = self.lines[j]
            if line:
                self.win.addstr(i, 1, line+' '*(self.max_width-len(line)))
                i += 1
        self.refresh()
