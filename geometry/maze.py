import random
import time

from geometry.cell import Cell
from geometry.line import Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1  # The x-coordinate of the starting point
        self.y1 = y1  # The y-coordinate of the starting point
        self.num_rows = num_rows  # The number of rows in the grid
        self.num_cols = num_cols  # The number of columns in the grid
        self.cell_size_x = cell_size_x  # The width of each grid cell
        self.cell_size_y = cell_size_y  # The height of each grid cell
        if seed is not None:
            random.seed(seed)
        self.window = window  # The window object where the grid will be displayed
        self.__create_cells()

    def __create_cells(self):
        self._cells = [[0 for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                next_p = Point(self.x1, self.y1) + Point(i * self.cell_size_x, j * self.cell_size_y)
                cell = Cell([True, True, True, True], next_p, next_p + Point(self.cell_size_x, self.cell_size_y),
                            self.window)
                self._cells[i][j] = cell
                self.__draw_cell(i, j)
        self._break_entrance_and_exit()
        start_time = time.time()
        self._break_wall_r(0, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        self._reset_cells_visited()

    def _break_entrance_and_exit(self):
        if self.window is None:
            return
        self._cells[0][0].has_left_wall = False
        self.__draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __draw_cell(self, i, j):

        if self.window is not None:
            self._cells[i][j].draw()
            self.__animate()

    def __animate(self):
        self.window.redraw()
        time.sleep(0.03)
    def _reset_cells_visited(self):

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited=False
    def _break_wall_r(self, i, j):
        if self.window is None:
            return
        ref = self._cells[i][j]
        ref.visited = True
        last = self._cells[self.num_cols-1][self.num_rows-1]

        while True:
            if last.visited:
                return
            adjacents = []
            top = None
            pt = Point(0, 0)
            bottom = None
            pb = Point(0, 0)
            left = None
            pl = Point(0, 0)
            right = None
            pr = Point(0, 0)
            try:
                if j > 0:
                    top = self._cells[i][j - 1]
                    pt = Point(i, j - 1)
                    if not top.visited:
                        adjacents.append(top)
            except Exception as e:
                pass
            try:
                if j < len(self._cells[0]) - 1:
                    bottom = self._cells[i][j + 1]
                    pb = Point(i, j + 1)
                    if not bottom.visited:
                        adjacents.append(bottom)
            except Exception as e:
                pass
            try:
                if i > 0:
                    left = self._cells[i - 1][j]
                    pl = Point(i - 1, j)
                    if not left.visited:
                        adjacents.append(left)
            except Exception as e:
                pass
            try:
                if i < len(self._cells) - 1:
                    right = self._cells[i + 1][j]
                    pr = Point(i + 1, j)
                    if not right.visited:
                        adjacents.append(right)

            except Exception as e:
                pass
            if len(adjacents) == 0:
                ref.draw()
                return

            adj_to_go = random.choice(adjacents)
            adj_to_go_indexes = None
            if left is not None and adj_to_go == left:
                ref.has_left_wall = False
                left.has_right_wall = False

                adj_to_go_indexes = pl

            if top is not None and adj_to_go == top:
                ref.has_top_wall = False
                top.has_bottom_wall = False
                adj_to_go_indexes = pt

            if right is not None and adj_to_go == right:
                ref.has_right_wall = False
                right.has_left_wall = False
                adj_to_go_indexes = pr

            if bottom is not None and adj_to_go == bottom:
                ref.has_bottom_wall = False
                bottom.has_top_wall = False
                adj_to_go_indexes = pb

            ref.draw()
            adj_to_go.draw()
            self.__animate()

            if adj_to_go_indexes is not None:
                self._break_wall_r(adj_to_go_indexes.x, adj_to_go_indexes.y)

    def solver(self):
        return self.__solve_r(0,0)

    #TODO:SOLVE MAZE
    def __solve_r(self,i,j):
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        self.__animate()
        ref = self._cells[i][j]
        ref.visited=True
        adjs = self.get_adjacents(i,j)
        for adj in adjs:
            adjacent_cell = self._cells[adj.x][adj.y]
            if not adjacent_cell.visited and self.has_road_between(i,j,adjacent_cell):
                ref.draw_move(adjacent_cell)
                result = self.__solve_r(adj.x,adj.y)
                if result:
                    return True
                ref.draw_move(adjacent_cell,True)
        return False

    def get_adjacents(self,i,j):
        ref = self._cells[i][j]
        if ref is None:
            return
        adjacents = []

        if j > 0:
            pt = Point(i, j - 1)
            adjacents.append(pt)

        if j < len(self._cells[0]) - 1:
            pb = Point(i, j + 1)
            adjacents.append(pb)

        if i > 0:
            pl = Point(i - 1, j)
            adjacents.append(pl)

        if i < len(self._cells) - 1:
            pr = Point(i + 1, j)
            adjacents.append(pr)


        return adjacents
    def has_road_between(self,i,j,cell2: Cell):
        ref = self._cells[i][j]
        adjs = self.get_adjacents(i,j)
        cell2pos=None

        for adj in adjs:
            if self._cells[adj.x][adj.y] == cell2:
                cell2pos = Point(adj.x,adj.y)
        if cell2pos is None:
            return False
        adj=cell2pos
        top_adj = j - adj.y == 1
        bottom_adj = adj.y-j == 1
        letf_adj=i-adj.x == 1
        right_adj=adj.x-i==1
        if letf_adj and not ref.has_left_wall and not cell2.has_right_wall:
            return True
        if right_adj and not ref.has_right_wall and not cell2.has_left_wall:
            return True
        if top_adj and not ref.has_top_wall and not cell2.has_bottom_wall:
            return True
        if bottom_adj and not ref.has_bottom_wall and not cell2.has_top_wall:
            return True
        return False














