import unittest

# assuming your `Maze` class is in a file called `maze.py`
from lib.maze import Maze
from lib.window import Window

class Tests(unittest.TestCase):
    win = Window(800, 600)
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
