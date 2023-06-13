import math

AI_PLAYER = "X"
HUMAN_PLAYER = "O"
EMPTY = " "

def make_move(board_state, move, player):
    """
    This function makes a move for the given player on the given board_state
    and returns the new board state.
    """
    return board_state[:move] + player + board_state[move+1:]

def get_possible_moves(board_state):
    """
    This function returns a list of possible moves on the given board state.
    """
    return [i for i, s in enumerate(board_state) if s == EMPTY]

def get_winner(board_state):
    """
    This function checks the board state to see if there is a winner.
    If there is a winner, it returns the player who won. Otherwise, it returns None.
    """
    for i in range(3):
        row = board_state[i*3:(i+1)*3]
        if row.count(HUMAN_PLAYER) == 3:
            return HUMAN_PLAYER
        elif row.count(AI_PLAYER) == 3:
            return AI_PLAYER
    for i in range(3):
        col = board_state[i::3]
        if col.count(HUMAN_PLAYER) == 3:
            return HUMAN_PLAYER
        elif col.count(AI_PLAYER) == 3:
            return AI_PLAYER
    diag1 = board_state[0:9:4]
    if diag1.count(HUMAN_PLAYER) == 3:
        return HUMAN_PLAYER
    elif diag1.count(AI_PLAYER) == 3:
        return AI_PLAYER
    diag2 = board_state[2:7:2]
    if diag2.count(HUMAN_PLAYER) == 3:
        return HUMAN_PLAYER
    elif diag2.count(AI_PLAYER) == 3:
        return AI_PLAYER
    if EMPTY not in board_state:
        return "draw"
    return None

def minimax_with_alpha_beta_pruning(board_state, depth, alpha, beta, maximizing_player):
    """
    This function uses the minimax algorithm with alpha-beta pruning to determine
    the best move for the AI player on the given board state.
    """
    if depth == 0 or get_winner(board_state) is not None:
        return None, evaluate_board_state(board_state, AI_PLAYER)

    possible_moves = get_possible_moves(board_state)

    if maximizing_player:
        max_value = -math.inf
        best_move = None
        for move in possible_moves:
            new_board_state = make_move(board_state, move, AI_PLAYER)
            _, value = minimax_with_alpha_beta_pruning(new_board_state, depth-1, alpha, beta, False)
            if value > max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return best_move, max_value
    else:
        min_value = math.inf
        best_move = None
        for move in possible_moves:
            new_board_state = make_move(board_state, move, HUMAN_PLAYER)
            _, value = minimax_with_alpha_beta_pruning(new_board_state, depth-1, alpha, beta, True)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return best_move, min_value

    
def evaluate_board_state(board_state, player):
    """
    This function evaluates the given board state from the perspective of the AI player.
    """
    score = 0
    # Check rows
    for i in range(3):
        row = board_state[i*3:(i+1)*3]
        score += evaluate_sequence(row, player)
    # Check columns
    for i in range(3):
        col = board_state[i::3]
        score += evaluate_sequence(col, player)
    # Check diagonals
    diag1 = board_state[0:9:4]
    score += evaluate_sequence(diag1, player)
    diag2 = board_state[2:7:2]
    score += evaluate_sequence(diag2, player)
    return score

def evaluate_sequence(sequence, player):
    """
    This function evaluates a sequence of three cells for the given player.
    """
    if sequence.count(player) == 3:
        return 100
    elif sequence.count(player) == 2 and sequence.count(EMPTY) == 1:
        return 10
    elif sequence.count(player) == 1 and sequence.count(EMPTY) == 2:
        return 1
    elif sequence.count(HUMAN_PLAYER) == 2 and sequence.count(EMPTY) == 1:
        return -10
    elif sequence.count(HUMAN_PLAYER) == 1 and sequence.count(EMPTY) == 2:
        return -1
    else:
        return 0

def play_tic_tac_toe():
    """
    This function allows the user to play tic-tac-toe against the AI player.
    """
    board_state = EMPTY * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board_state(board_state)
    while True:
        # Player move
        move = None
        while move not in get_possible_moves(board_state):
            try:
                move = int(input("Enter your move (1-9): ")) - 1
            except ValueError:
                pass
        board_state = make_move(board_state, move, HUMAN_PLAYER)
        print_board_state(board_state)
        winner = get_winner(board_state)
        if winner is not None:
            print("Game over. Winner: " + winner)
            break
        # AI move
        move, _ = minimax_with_alpha_beta_pruning(board_state, depth=5, alpha=-math.inf, beta=math.inf, maximizing_player=True)
        board_state = make_move(board_state, move, AI_PLAYER)
        print("AI move:", move+1)
        print_board_state(board_state)
        winner = get_winner(board_state)
        if winner is not None:
            print("Game over. Winner: " + winner)
            break

def print_board_state(board_state):
    """
    This function prints the given board state to the console.
    """
    for i in range(3):
        print(board_state[i*3:(i+1)*3])
    print()

if __name__ == "__main__":
    play_tic_tac_toe()
