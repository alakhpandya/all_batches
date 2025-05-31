board = [[' ' for x in range(3)] for y in range(3)]

def print_board():
    for row in board:
        print("|".join(row))
    print("\n")

def check_win():
    # Check rows
    for row in board:
        if row == ['X', 'X', 'X']:
            return 'X'
        elif row == ['O', 'O', 'O']:
            return 'O'
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def check_tie():
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

def get_computer_move():
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = 'O'

def minimax(board, maximizing_player):
    winner = check_win()
    if winner:
        if winner == 'O':
            return 1
        else:
            return -1
    if check_tie():
        return 0
    if maximizing_player:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

player = 'X'
winner = None



while not winner and not check_tie():
    print_board()
    if player == 'X':
        print("Your turn. Enter row and column, separated by a space:")
        row, col = [int(x) for x in input().strip().split()]
        while board[row][col] != ' ':
            print("That cell is already occupied. Enter another row and column:")
            row, col = [int(x) for x in input().strip().split()]
        board[row][col] = player
    else:
        get_computer_move()
        print("Computer's turn:")
        print_board()
    player = 'X' if player == 'O' else 'O'
    winner = check_win()

if winner:
    print("{} won!".format(winner))
else:
    print("It's a tie!")

