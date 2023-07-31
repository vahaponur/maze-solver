from geometry.window import *
from geometry.cell import Cell

window = Window(800, 600)
grid_row = 8
grid_column = 6
next_p = Point(0, 0)
line_width = 100
line_height = 100
ref_p = Point(line_width, line_height)
last_cell = None
for i in range(grid_row):
    for j in range(grid_column):
        next_p = Point(i * line_width, j * line_height)
        cell = Cell([True, True, True, True], next_p, next_p + Point(ref_p.x, ref_p.y), window)
        cell.draw()
        if last_cell is not None:
            last_cell.draw_move(cell, True)
        last_cell = cell

window.wait_for_close()
