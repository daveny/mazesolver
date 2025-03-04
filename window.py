from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        # self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        # self.running = True
        # while self.running:
        #     self.redraw()
        self.root.mainloop()

    def close(self):
        # self.running = False
        self.root.quit()
        self.root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)