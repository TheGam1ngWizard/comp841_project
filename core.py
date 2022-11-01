# https://towardsdatascience.com/lets-beat-games-using-a-bunch-of-code-part-1-tic-tac-toe-1543e981fec1
    # Python(2?) code adapted/found at: https://github.com/agrawal-rohit/tic-tac-toe-bot
# https://geekflare.com/tic-tac-toe-python-code/
import sys
import numpy as np
from math import inf as infinity
import itertools
import random
import time


class TicTacToe:
    def __init__(self):
        self.tic_tac_board = [[' ', ' ', ' '],
                              [' ', ' ', ' '],
                              [' ', ' ', ' ']]
        self.players = ['X', 'O']


    def play_move(self, player, block_num):
        if self.tic_tac_board[int((block_num - 1)/3)][(block_num - 1)%3] == ' ':
            self.tic_tac_board[int((block_num - 1)/3)][(block_num - 1)%3] = player
        else:
            block_num = int(input(f"Tile is not empty, chose again: "))
            self.play_move(player, block_num)


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

        # Choose Starting Player & Set gamestate to 'not won'
        player_choice = input("Choose which player goes first - X or O: ")
        winner = None
        
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
            # Choose move
            block_choice = int(input(
                str(self.players[current_player_idx]) + "'s Turn! Choose where to place (1 to 9): "))
            self.play_move(self.players[current_player_idx], block_choice)
            self.print_board()
            current_state = self.current_board()
            
            # debug
            print(str(current_state))
            
            # These provide the exact same results
            # print(self.players[current_player_idx])
            # print(str(self.players[current_player_idx]))
            
            # TODO: Fix 'draw' state/end state problem
            if current_state == "Not Done":
                current_player_idx = (current_player_idx + 1) % 2
            elif current_state == "Done":
                print(self.players[current_player_idx] + " won!")
            else:
                print("Draw!")
                
                


# Running the project
game = TicTacToe()
game.run_game()