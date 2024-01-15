#Automated Hash-Game (Jogo da Velha) - First Test
#Designed by Leonardo de Sousa Marques

#Import random library;
from random import randrange, choice

#Board Class;
class Board:
    @staticmethod
    def Board3per3():
        # Create a 3x3 board initialized with None
        tab = [[None] * 3 for _ in range(3)]
        return tab

class Game:
    @staticmethod
    def ChecksWinner(tab):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if tab[i][0] == tab[i][1] == tab[i][2] is not None:
                return True, tab[i][0], 'row '+ str(i + 1)
            if tab[0][i] == tab[1][i] == tab[2][i] is not None:
                return True, tab[0][i], 'column ' + str(i + 1)
        if tab[0][0] == tab[1][1] == tab[2][2] is not None:
            return True, tab[0][0], 'diagonal 1'
        if tab[0][2] == tab[1][1] == tab[2][0] is not None:
            return True, tab[0][2], 'diagonal 2'
        if all(cell is not None for row in tab for cell in row):
            return True, "None", "Tie"
        return False, "None", "None"

    @staticmethod
    def Play(tab):
        # 0 => circle, 1 => x;
        while True:
            plays = [0, 1]

            for _ in range(9):
                i = randrange(3)
                j = randrange(3)
                if tab[i][j] is None:
                    tab[i][j] = choice(plays)
                # Check if the game ended:
                end, winner, place = Game.ChecksWinner(tab)
                if end:
                    print(winner, "won the game in", place)
                    return  # Exit the Play function
            # If no winner found after 9 moves, reset the board
            tab = Board.Board3per3()

if __name__ == "__main__":
    board = Board.Board3per3()
    Game.Play(board)
