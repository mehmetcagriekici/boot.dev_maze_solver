import time
import random

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
            seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = random.seed(seed) if seed else 0

        self.__cells = list()
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.__animate()

        self.__cells[i][j].visited = True

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        curr_cell = self.__cells[i][j]  
        if i > 0:
            next_cell = self.__cells[i-1][j]
            if not curr_cell.has_left_wall and not next_cell.has_right_wall and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                res = self.__solve_r(i-1, j)
                if res:
                    return res
                curr_cell.draw_move(next_cell, undo=True)

        if i < self.__num_cols - 1:
            next_cell = self.__cells[i+1][j]
            if not curr_cell.has_right_wall and not next_cell.has_left_wall and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                res = self.__solve_r(i+1, j)
                if res:
                    return res
                curr_cell.draw_move(next_cell, undo=True)

        if j < self.__num_rows - 1:
            next_cell = self.__cells[i][j+1]
            if not curr_cell.has_bottom_wall and not next_cell.has_top_wall and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                res = self.__solve_r(i, j+1)
                if res:
                    return res
                curr_cell.draw_move(next_cell, undo=True)

        if j > 0:
            next_cell = self.__cells[i][j-1]
            if not curr_cell.has_top_wall and not next_cell.has_bottom_wall and not next_cell.visited:
                curr_cell.draw_move(next_cell)
                res = self.__solve_r(i, j-1)
                if res:
                    return res
                curr_cell.draw_move(next_cell, undo=True)

        return False

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

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False
                
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(0, 0)
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            neighbors = list()
            
            up = j - 1 if j > 0 else 0
            right = i + 1 if i < self.__num_cols - 1 else self.__num_cols - 1
            down = j + 1 if j < self.__num_rows - 1 else self.__num_rows - 1
            left = i - 1 if i > 0 else 0

            if not self.__cells[i][up].visited:
                neighbors.append("up")

            if not self.__cells[right][j].visited:
                neighbors.append("right")

            if not self.__cells[i][down].visited:
                neighbors.append("down")

            if not self.__cells[left][j].visited:
                neighbors.append("left")

            if len(neighbors) == 0:
                return

            idx = random.randrange(0, len(neighbors))
            if neighbors[idx] == "up":
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][up].has_bottom_wall = False
                self.__draw_cell(i, up)
                self.__draw_cell(i, j)
                self.__break_walls_r(i, up)

            if neighbors[idx] == "right":
                self.__cells[i][j].has_right_wall = False
                self.__cells[right][j].has_left_wall = False
                self.__draw_cell(right, j)
                self.__draw_cell(i, j)
                self.__break_walls_r(right, j)

            if neighbors[idx] == "down":
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][down].has_top_wall = False
                self.__draw_cell(i, down)
                self.__draw_cell(i, j)
                self.__break_walls_r(i, down)

            if neighbors[idx] == "left":
                self.__cells[i][j].has_left_wall = False
                self.__cells[left][j].has_right_wall = False
                self.__draw_cell(left, j)
                self.__draw_cell(i, j)
                self.__break_walls_r(left, j)

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
        
