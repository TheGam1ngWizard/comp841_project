# https://towardsdatascience.com/lets-beat-games-using-a-bunch-of-code-part-1-tic-tac-toe-1543e981fec1
    # Python(2?) code adapted/found at: https://github.com/agrawal-rohit/tic-tac-toe-bot

# While I could have stolen the minimax code from the above, I actually found this article on it (https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/) that both shows the code, and explains how it works.

# https://geekflare.com/tic-tac-toe-python-code/
# import sys
# import numpy as np
# from math import inf as infinity
# import itertools
# import random
# import time


class TicTacToe:
    def __init__(self):
        # Initialize an empty gameboard, and our 'players' to go along. Theoretically this means we could increase the size of our board, and the number of players along with it, however this would require major changes elsewhere.
        self.tic_tac_board = [[' ', ' ', ' '],
                              [' ', ' ', ' '],
                              [' ', ' ', ' ']]
        self.players = ['X', 'O']


    def play_move(self, player, row, col):
        if self.tic_tac_board[row - 1][col - 1] == ' ':
            self.tic_tac_board[row - 1][col - 1] = player
        else:
            row = int(input(f"Tile is not empty, chose new row: "))
            col = int(input(f"Tile is not empty, chose new col: "))
            self.play_move(player, row, col)


    def current_board(self):
        # Check horizontals
        if (self.tic_tac_board[0][0] == self.tic_tac_board[0][1] and self.tic_tac_board[0][1] == self.tic_tac_board[0][2] and self.tic_tac_board[0][0] != ' '):
            return "Done"
        if (self.tic_tac_board[1][0] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[1][2] and self.tic_tac_board[1][0] != ' '):
            return "Done"
        if (self.tic_tac_board[2][0] == self.tic_tac_board[2][1] and self.tic_tac_board[2][1] == self.tic_tac_board[2][2] and self.tic_tac_board[2][0] != ' '):
            return "Done"

        # Check verticals
        if (self.tic_tac_board[0][0] == self.tic_tac_board[1][0] and self.tic_tac_board[1][0] == self.tic_tac_board[2][0] and self.tic_tac_board[0][0] != ' '):
            return "Done"
        if (self.tic_tac_board[0][1] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[2][1] and self.tic_tac_board[0][1] != ' '):
            return "Done"
        if (self.tic_tac_board[0][2] == self.tic_tac_board[1][2] and self.tic_tac_board[1][2] == self.tic_tac_board[2][2] and self.tic_tac_board[0][2] != ' '):
            return "Done"

        # Check diagonals
        if (self.tic_tac_board[0][0] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[2][2] and self.tic_tac_board[0][0] != ' '):
            return "Done"
        if (self.tic_tac_board[2][0] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[0][2] and self.tic_tac_board[2][0] != ' '):
            return "Done"

        # Check Draw State
        should_draw = 0
        for row in range(3):
            for col in range(3):
                if self.tic_tac_board[row][col] == ' ':
                    should_draw = 1
        if should_draw == 0:
            return "Draw"

        return "Not Done"


    def print_board(self):
        print('----------------')
        print('| ' + str(self.tic_tac_board[0][0]) + ' || ' + str(
            self.tic_tac_board[0][1]) + ' || ' + str(self.tic_tac_board[0][2]) + ' |')
        print('----------------')
        print('| ' + str(self.tic_tac_board[1][0]) + ' || ' + str(
            self.tic_tac_board[1][1]) + ' || ' + str(self.tic_tac_board[1][2]) + ' |')
        print('----------------')
        print('| ' + str(self.tic_tac_board[2][0]) + ' || ' + str(
            self.tic_tac_board[2][1]) + ' || ' + str(self.tic_tac_board[2][2]) + ' |')
        print('----------------')


   

    # PLaying


    def run_game(self):

        # Startup
        current_state = "Not Done"
        print(f"New Game!")

        # Show Blank Gameboard
        self.print_board()

        # Choose Starting Player
        player_choice = input("Choose which player goes first - X or O: ")
        
        # Init Playerstate
        if player_choice == 'X' or player_choice == 'x':
            current_player_idx = 0
        elif player_choice == 'O' or player_choice == 'o':
            current_player_idx = 1
        else: 
            print(f"That is not a valid choice, please try again.")
            self.run_game()

        # Rungame
        while current_state == "Not Done":
            '''
            # Choose move validator
            row_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Row to place in: ")
            while not row_choice.isnumeric():
                print("Your choice needs to be a number.")
                row_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Row to place in: ")
            
            col_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Col to place in: ")
            while not col_choice.isnumeric():
                print("Your choice needs to be a number.")
                col_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Col to place in: ")

            while int(row_choice) > len(self.tic_tac_board):
                print("Your choice needs to be within the size of the board.")
                row_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Row to place in: ")

            while int(col_choice) > len(self.tic_tac_board):
                print("Your choice needs to be within the size of the board.")
                col_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Col to place in: ")
            '''

            numeric = False
            valid = False

            while numeric != True and valid != True:
                row_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Row to place in: ")
                col_choice = input((self.players[current_player_idx]) + "'s Turn! Choose which Col to place in: ")

                if row_choice.isnumeric() and col_choice.isnumeric():
                    numeric = True
                else:
                    print(f"One of your choices weren't Numeric! Try again.")
                    continue                
                if int(row_choice) < len(self.tic_tac_board) and int(col_choice) < len(self.tic_tac_board):
                    valid = True
                else:
                    print(f"One of your choices weren't within the bounds of the game! Try again.")
                    continue
                    


            '''
            block_choice = int(input(
                str(self.players[current_player_idx]) + "'s Turn! Choose where to place (1 to 9): "))  
            '''

            row = int(row_choice)
            col = int(col_choice)

            self.play_move(self.players[current_player_idx], row, col)
            self.print_board()
            current_state = self.current_board()
            
            # Nick TODO: Theoretical rewrite of the 'win' condition checker.
            # current_state = win.current_board(self.tic_tac_board)

            # debug
            print(str(current_state))
            
            # These provide the exact same results
            # print(self.players[current_player_idx])
            # print(str(self.players[current_player_idx]))
            
            if current_state == "Not Done":
                current_player_idx = (current_player_idx + 1) % 2
            elif current_state == "Done":
                print(self.players[current_player_idx] + " won!")
            else:
                print("Draw!")
                
                


# Running the project
game = TicTacToe()
game.run_game()