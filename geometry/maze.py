import time

from geometry.cell import Cell
from geometry.line import Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x,cell_size_y, window):
        self.x1 = x1  # The x-coordinate of the starting point
        self.y1 = y1  # The y-coordinate of the starting point
        self.num_rows = num_rows  # The number of rows in the grid
        self.num_cols = num_cols  # The number of columns in the grid
        self.cell_size_x = cell_size_x  # The width of each grid cell
        self.cell_size_y = cell_size_y  # The height of each grid cell
        self.window = window  # The window object where the grid will be displayed
        self.__create_cells()
    def __create_cells(self):
        self.__cells = [0 for _ in range(self.num_rows * self.num_cols)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__cells[i*j]=self.__draw_cell( i, j)
    def __draw_cell(self,i,j):
        next_p = Point(self.x1, self.y1) + Point(i * self.cell_size_x, j * self.cell_size_y)
        cell = Cell([True, True, True, True], next_p, next_p + Point(self.cell_size_x, self.cell_size_y), self.window)
        cell.draw()
        self.__animate()
        return cell
    def __animate(self):
        self.window.redraw()
        time.sleep(0.1)
