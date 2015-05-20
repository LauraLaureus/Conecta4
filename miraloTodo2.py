
def miraloTodo(state):
    if state.utility != 0 and state.to_move == 'X':
        return state.utility
    if state.utility != 0 and state.to_move == 'O':
        return -state.utility

    board = state.board
    h = 0
    for row in range(1, state.row+1):
        in_row = state.k
        for column in range(1, state.column+1):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
            if in_row <= 0:
                h += 1
                in_row = state.k

    # por columnas

    for column in range(1, state.column+1):
        in_row = state.k
        for row in range(1, state.row+1):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
            if in_row <= 0:
                h += 1
                in_row= state.k


    #por diagonales
    for row in range(1, state.row-2):
        in_row = state.k
        for column in range(1, state.column-2):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                for p in range(1, state.k):
                    if board.get((row + p, column + p)) == state.to_move or (
                                    board.get((row + p, column + p)) == None and board.get(
                                    (row + p, column + p)) in state.legal_moves):
                        h += 1

    for row in range(1, state.row-2):
        in_row = state.k
        for column in range(state.column-3, state.column+1):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                for p in range(1, state.k):
                    if board.get((row + p, column - p)) == state.to_move or (
                                    board.get((row + p, column - p)) == None and board.get(
                                    (row + p, column - p)) in state.legal_moves):
                        h += 1

    return h
