from tkinter import Tk, BOTH, Canvas
from line import *

class Window:
    def __init__(self, width, height):
        self.__root = Tk(className=' Maze Solver')
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOWS",self.close() )
        self.canvas = Canvas(self.__root,height=height,width=width,bg="white")
        self.canvas.pack(fill=BOTH,expand=True)
        self.running = False
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    def draw_line(self, line: Line, fillcolor):
        line.draw(self.canvas, fillcolor)



    def close(self):
        self.running=False



