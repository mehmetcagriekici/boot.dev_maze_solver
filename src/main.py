from lib.window import Window
from lib.maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(200, 150, 5, 6, 20, 20, win)
    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
