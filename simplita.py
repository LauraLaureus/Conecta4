def heuristica(state):
    if state.utility !=0 and state.to_move == 'X':
        return state.utility
    elif state.utility != 0 and state.to_move== 'O':
        return  -state.utility
    h = 0
    for tuple in state.legal_moves:
        weight = 10
        if tuple[0] == 6:
            h += 5
            continue
        for row_prima in range(tuple[0], 6):
            if state.board.get((row_prima + 1, tuple[1])) != state.to_move:
                break
            h += weight
            weight += 10

    return h
