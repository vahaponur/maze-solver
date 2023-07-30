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

    def __init__(self, has_walls, ptl, pbr, window):
        self.has_left_wall = has_walls[0]
        self.has_right_wall = has_walls[1]
        self.has_top_wall = has_walls[2]
        self.has_bottom_wall = has_walls[3]
        self.__ptl = ptl
        self.__pbr = pbr
        self.__window = window

    def draw(self):
        if self.has_left_wall:
            left_line=Line(self.__ptl, Point(self.__ptl.x,self.__pbr.y))
            self.__window.draw_line(left_line,"red")
        if self.has_right_wall:
            right_line = Line(Point(self.__pbr.x,self.__ptl.y), self.__pbr)
            self.__window.draw_line(right_line, "red")
        if self.has_top_wall:
            top_line = Line(self.__ptl, Point(self.__pbr.x,self.__ptl.y))
            self.__window.draw_line(top_line, "red")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self.__ptl.x,self.__pbr.y),self.__pbr)
            self.__window.draw_line(bottom_line, "red")

