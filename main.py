from maze import Maze
from point import Cell, Line, Point
from window import Window

def main():
    win = Window(800, 600)

    # line1 = Line(Point(0, 0), Point(100, 100))
    # line2 = Line(Point(100, 100), Point(200, 0))
    #
    # cell1 = Cell(10, 100, 10, 100, True, True, True, True, win)
    # cell2 = Cell(110, 200, 110, 200, True, True, False, False, win)
    #
    # win.draw_line(line1, "red")
    # win.draw_line(line2, "blue")
    #
    # cell1.draw()
    # cell2.draw()
    #
    # cell1.draw_move(cell2, True)

    maze = Maze(150, 50, 20, 20, 25, 25, win)
    

    win.wait_for_close()
    return 0

main()