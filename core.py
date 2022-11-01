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
            block_num = int(input(f"Tile note empty, chose again: "))
            self.play_move(player, block_num)


    def current_board(self, tic_tac_board):

        should_draw = 0
        for row in range(3):
            for col in range(3):
                if self.tic_tac_board[row][col] == ' ':
                    should_draw = 1
        if should_draw == 0:
            return None, "Draw"

        # Check horizontals
        if (self.tic_tac_board[0][0] == self.tic_tac_board[0][1] and self.tic_tac_board[0][1] == self.tic_tac_board[0][2] and self.tic_tac_board[0][0] != ' '):
            return tic_tac_board[0][0], "Done"
        if (self.tic_tac_board[1][0] == self.tic_tac_board[1][1] and tic_tac_board[1][1] == self.tic_tac_board[1][2] and self.tic_tac_board[1][0] != ' '):
            return self.tic_tac_board[1][0], "Done"
        if (self.tic_tac_board[2][0] == self.tic_tac_board[2][1] and self.tic_tac_board[2][1] == self.tic_tac_board[2][2] and self.tic_tac_board[2][0] != ' '):
            return self.tic_tac_board[2][0], "Done"

        # Check verticals
        if (self.tic_tac_board[0][0] == self.tic_tac_board[1][0] and tic_tac_board[1][0] == self.tic_tac_board[2][0] and self.tic_tac_board[0][0] != ' '):
            return tic_tac_board[0][0], "Done"
        if (self.tic_tac_board[0][1] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[2][1] and self.tic_tac_board[0][1] != ' '):
            return self.tic_tac_board[0][1], "Done"
        if (self.tic_tac_board[0][2] == self.tic_tac_board[1][2] and self.tic_tac_board[1][2] == self.tic_tac_board[2][2] and self.tic_tac_board[0][2] != ' '):
            return self.tic_tac_board[0][2], "Done"

        # Check diagonals
        if (self.tic_tac_board[0][0] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[2][2] and self.tic_tac_board[0][0] != ' '):
            return self.tic_tac_board[1][1], "Done"
        if (self.tic_tac_board[2][0] == self.tic_tac_board[1][1] and self.tic_tac_board[1][1] == self.tic_tac_board[0][2] and self.tic_tac_board[2][0] != ' '):
            return self.tic_tac_board[1][1], "Done"

        return None, "Not Done"


    def print_board(self, tic_tac_board):
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
        current_state = "Not Done"
        print(f"New Game!")
        self.print_board(self.tic_tac_board)
        player_choice = input("Choose which player goes first - X or O: ")
        winner = None
        if player_choice == 'X' or player_choice == 'x':
            current_player_idx = 0
        else:
            current_player_idx = 1
        while current_state == "Not Done":
            block_choice = int(input(
                str(self.players[current_player_idx]) + "'s Turn! Choose where to place (1 to 9): "))
            self.play_move(self.players[current_player_idx], block_choice)
            self.print_board(self.tic_tac_board)
            winner, current_state = self.current_board(self.tic_tac_board)
            if winner != None:
                print(str(winner) + " won!")
            else:
                current_player_idx = (current_player_idx + 1) % 2

            if current_state == "Draw":
                print("Draw!")


# Running the project
game = TicTacToe()
game.run_game()