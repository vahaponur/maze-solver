from geometry.window import *
from geometry.maze import Maze

window = Window(800, 600)
maze =Maze(10,10,7,7,30,30,window)

window.wait_for_close()
