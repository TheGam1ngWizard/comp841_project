def is_win(cond, player):
    if cond == True:
        if player != " ":
            return True
    return False

def check_for_win(board):
    win = True
    board_size = len(board)

    # check rows for win
    for row in range(board_size):
        player = board[row][0]
        for column in range(board_size):
            if board[row][column] != player:
                win = False
                break
        if is_win(win, player):
            return player
        win = True # reset flag

    # check columns for win
    for column in range(board_size): # rows and columns same length
        player = board[0][column]
        for row in board:
            if row[column] != player:
                win = False
                break
        if is_win(win, player):
            return player
        win = True # reset flag
    
    # check diagonals for win
    # top left to bottom right
    player = board[0][0]
    for diag in range(board_size):
        if board[diag][diag] != player:
            win = False
            break
    if is_win(win, player):
        return player
    win = True # reset flag

    # bottom left to top right
    player = board[board_size - 1][0]
    row = 0
    for column in range(board_size - 1, 0, -1):
        if board[row][column] != player:
            win = False
            break
        row += 1
    if is_win(win, player):
        return player

    return "No winner."
