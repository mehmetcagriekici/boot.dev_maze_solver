import time

from lib.cell import Cell

class Maze:
    def __init__(
                    self,
                    x1,
                    y1,
                    num_rows,
                    num_cols,
                    cell_size_x,
                    cell_size_y,
                    win,
                ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = list()
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = i * self.__cell_size_x + self.__x1
        x2 = x1 + self.__cell_size_x
        y1 = j * self.__cell_size_y + self.__y1
        y2 = y1 + self.__cell_size_y

        self.__cells[i][j].draw(x1, x2, y1, y2)

        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
        
