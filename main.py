from geometry.window import *
from geometry.maze import Maze

window = Window(800, 600)
maze =Maze(10,10,10,10,60,60,window,1)

window.wait_for_close()
