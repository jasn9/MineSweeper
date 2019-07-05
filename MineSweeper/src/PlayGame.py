

# Game is started

from Grid import Grid

from MinesGenerator import MinesGenerator

class PlayGame :

    def __init__(self):

        mines = MinesGenerator(20,10)
        mineslist = mines.Mines()
        grid = Grid(20,10,mineslist)


Play = PlayGame()


