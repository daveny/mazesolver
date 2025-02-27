class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win = None):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.win = win

    def draw(self, x1, y1, x2, y2):

        if self.win is None or self.win.canvas is None:
            # Skip drawing if no valid window object or canvas exists.
            return

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        if self.has_left_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="black")
        if not self.has_left_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="white")

        if self.has_top_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="black")
        if not self.has_top_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="white")

        if self.has_right_wall:
            self.win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="black")
        if not self.has_right_wall:
            self.win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="white")

        if self.has_bottom_wall:
            self.win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="black")
        if not self.has_bottom_wall:
            self.win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="white")

    def s_draw(self):
        if self.x1 is None or self.x2 is None or self.y1 is None or self.y2 is None:
            return
        self.draw(self.x1, self.y1, self.x2, self.y2)

    def draw_move(self, to_cell, undo=False):
        move = Line(Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2), Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2))
        if undo:
            move.draw(self.win.canvas, "gray")
        else:
            move.draw(self.win.canvas, "red")
        