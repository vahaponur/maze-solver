from geometry.line import *


class Cell:
    """
    has wall takes a list of boolean
    list = [T,F,F,T]
    each of the term of the list corresponds
    has left wall=list[0]
    has right wall = list[1]
    has top wall = list[2]
    has bottom wall = list[3]
    ptl = position of top left corner (a point)
    pbr = position of bottom right corner
    """

    def __init__(self, has_walls, ptl, pbr, window=None):
        self.has_left_wall = has_walls[0]
        self.has_right_wall = has_walls[1]
        self.has_top_wall = has_walls[2]
        self.has_bottom_wall = has_walls[3]
        self.__ptl = ptl
        self.__pbr = pbr
        self.__window = window
        self.center = self.__ptl + (self.__pbr - self.__ptl) / 2
        self.visited = False

    def draw(self):
        left_line = Line(self.__ptl, Point(self.__ptl.x, self.__pbr.y))
        self.__window.draw_line(left_line, self.pick_color(self.has_left_wall))

        right_line = Line(Point(self.__pbr.x, self.__ptl.y), self.__pbr)
        self.__window.draw_line(right_line, self.pick_color(self.has_right_wall))

        top_line = Line(self.__ptl, Point(self.__pbr.x, self.__ptl.y))
        self.__window.draw_line(top_line, self.pick_color(self.has_top_wall))

        bottom_line = Line(Point(self.__ptl.x, self.__pbr.y), self.__pbr)
        self.__window.draw_line(bottom_line, self.pick_color(self.has_bottom_wall))
    def pick_color(self,has_wall):
        if has_wall:
            return "red"
        return 'white'
    def draw_move(self, to_cell, undo=False):
        color = 'gray' if undo else 'red'
        line = Line(self.center, to_cell.center)
        self.__window.draw_line(line, color)
