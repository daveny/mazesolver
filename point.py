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
    def __init__(self, x1, x2, y1, y2, has_left_wall, has_top_wall, has_right_wall, has_bottom_wall, win):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.win = win

    def draw(self):

        if self.has_left_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x1, self.y2)
        if self.has_top_wall:
            self.win.canvas.create_line(self.x1, self.y1, self.x2, self.y1)
        if self.has_right_wall:
            self.win.canvas.create_line(self.x2, self.y1, self.x2, self.y2)
        if self.has_bottom_wall:
            self.win.canvas.create_line(self.x1, self.y2, self.x2, self.y2)
        
    def draw_move(self, to_cell, undo=False):
        move = Line(Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2), Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2))
        if undo:
            move.draw(self.win.canvas, "gray")
        else:
            move.draw(self.win.canvas, "red")
        