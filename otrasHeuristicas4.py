def k_in_row(state, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    n = 0  # n is number of moves in row
    board = state.board
    player = state.to_move
    for move in state.legal_moves:
        x, y = move
        h=0
        delta_h =h
        while board.get((x, y)) == player or board.get((x,y)) == None:
            if board.get((x,y)) == None:
                h += 0.5
            else:
                h += 1
            x, y = x + delta_x, y + delta_y
            if h - delta_h >3.5:
                break
        x, y = move
        delta_h=h
        while board.get((x, y)) == player or board.get((x,y)) == None:
            if board.get((x,y)) == None:
                h += 0.5
            else:
                h += 1
            x, y = x - delta_x, y - delta_y
            if h - delta_h >3.5:
                break
        h -= 1  # Because we counted move itself twice
        if h >= 4:
            n+=h*50
        elif h>1.5:
            n+=h*25
    return n

def heuristic(state):
    "If X wins with this move, return 1; if O return -1; else return 0."
    if state.utility !=0 and state.to_move == 'X':
        return state.utility
    elif state.utility != 0 and state.to_move== 'O':
        return  -state.utility
    h=0
    h+=k_in_row(state, (0, 1))
    h+=k_in_row(state, (1, 0))
    h+=k_in_row(state, (1, -1))
    h+=k_in_row(state, (1, 1))

    return h