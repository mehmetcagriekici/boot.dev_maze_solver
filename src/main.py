from lib.window import Window
from lib.maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(200, 150, 20, 30, 20, 20, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
