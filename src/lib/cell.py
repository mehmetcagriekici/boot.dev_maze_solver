from lib.window import Window
from lib.draw_lines import Point, Line

class Cell:
    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_Wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = window

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            p1 = Point(x1, y1)
            p2 = Point(x1, y2)
            self.__draw_wall(p1, p2)
        
        if self.has_top_wall:
            p1 = Point(x1, y1)
            p2 = Point(x2, y1)
            self.__draw_wall(p1, p2)
        
        if self.has_right_wall:
            p1 = Point(x2, y1)
            p2 = Point(x2, y2)
            self.__draw_wall(p1, p2)
        
        if self.has_bottom_Wall:
            p1 = Point(x1, y2)
            p2 = Point(x2, y2)
            self.__draw_wall(p1, p2)

    def draw_move(self, to_cell, undo=False):
        center_self = self.__calc_center()
        center_to = to_cell.__calc_center()

        line = Line(center_self, center_to)

        fill = "gray"
        if undo:
            fill = "red"

        self.__win.draw_line(line, fill)

    def __draw_wall(self, p1: Point, p2: Point):
        line = Line(p1, p2)
        self.__win.draw_line(line, "black")

    def __calc_center(self):
        x = (self.__x1 + self.__x2) / 2
        y = (self.__y1 + self.__y2) / 2
        return Point(x, y)
