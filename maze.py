from point import Cell


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        lst = []
        for i in range(self.num_rows):
             for j in range(self.num_cols):
                 x1 = self.x1 + i * self.cell_size_x
                 x2 = x1 + self.cell_size_x
                 y1 = self.y1 + j * self.cell_size_y
                 y2 = y1 + self.cell_size_y
                 lst.append(Cell(x1, x2, y1, y2, True, True, True, True, self.win))
        self._cells = lst

        for item in self._cells:
            item.draw()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)