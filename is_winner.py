def check_for_win(board):
    win = True

    # check rows for win
    for row in range(len(board)):
        player = board[row][0]
        for column in range(len(board[row])):
            if board[row][column] != player:
                win = False
                break
        if win == True:
            if player != " ":
                return player
        win = True # reset flag

    # check columns for win
    for column in range(len(board)): # rows and columns same length
        player = board[0][column]
        for row in board:
            if row[column] != player:
                win = False
                break
        if win == True:
            if player != " ":
                return player
        win = True # reset flag
    
    return "No winner."