def neoHeuristic(state):
    if state.utility !=0 and state.to_move == 'X':
        return state.utility
    elif state.utility != 0 and state.to_move== 'O':
        return  -state.utility
    r = 7
    for tuple in state.legal_moves:
        if tuple[0] < r:
            r = tuple[0]

    board = state.board
    h = 0
    i = 0

    for x in range(r, 7):
        weight = 10
        weighti = 10
        move_x = 0
        move_y = 0
        for y in range(1, 8):
            movement = state.board.get((x, y))
            if movement == state.to_move:
                move_x += 1 * weight
                weight *= 2
                move_y = 0
                weighti = 10
            elif movement == None:
                if movement in state.legal_moves:
                    move_x += 1 * weight / 2
                    move_y += 1 * weighti / 2
                else:
                    move_x += 1 * weight / 3
                    move_y += 1 * weighti / 3
            else:
                move_y += 1 * weighti
                weighti *= 2
                move_x = 0
                weight = 10

        h += move_x
        i += move_y


    # por columnas

    for tuple in state.legal_moves:
        weight = 10
        weighti = 10
        move_x = 0
        move_y = 0
        if tuple[0] == 6:
            h += 5
            continue
        for row_prima in range(tuple[0], 6):
            if state.board.get((row_prima + 1, tuple[1])) == state.to_move:
                move_x += 1 * weight
                weight *= 2
                move_y = 0
                weighti = 10
            else:
                move_x = 0
                weight = 10
                move_y += 1 * weighti
                weighti *= 2
        h += move_x
        i += move_y

    #por diagonales

    for row in range(4, 7):
        weight = 10
        weighti = 10
        move_x = 0
        move_y = 0
        p = 0
        for column in range(1, row + 1):
            movement = state.board.get((row - p, column))
            if movement == state.to_move:
                move_x += 1 * weight
                weight *= 2
                move_y = 0
                weighti = 10
            elif movement == None:
                if movement in state.legal_moves:
                    move_x += 1 * weight / 2
                    move_y += 1 * weighti / 2
                else:
                    move_x += 1 * weight / 3
                    move_y += 1 * weighti / 3
            else:
                move_y += 1 * weighti
                weighti *= 2
                move_x = 0
                weight = 10
            p += 1

        p = 0
        for column in range(7, 1 + 8 - row, -1):
            movement = state.board.get((row - p, column))
            if movement == state.to_move:
                move_x += 1 * weight
                weight *= 2
                move_y = 0
                weighti = 10
            elif movement == None:
                if movement in state.legal_moves:
                    move_x += 1 * weight / 2
                    move_y += 1 * weighti / 2
                else:
                    move_x += 1 * weight / 3
                    move_y += 1 * weighti / 3
            else:
                move_y += 1 * weighti
                weighti *= 2
                move_x = 0
                weight = 10
            p += 1
        h += move_x
        i += move_y

    for column in range(2, 5):
        p = 0
        weight = 10
        weighti = 10
        move_x = 0
        move_y = 0
        for row in (6, column, -1):
            movement = state.board.get((row, column + p))
            if movement == state.to_move:
                move_x += 1 * weight
                weight *= 2
                move_y = 0
                weighti = 10
            elif movement == None:
                if movement in state.legal_moves:
                    move_x += 1 * weight / 2
                    move_y += 1 * weighti / 2
                else:
                    move_x += 1 * weight / 3
                    move_y += 1 * weighti / 3
            else:
                move_y += 1 * weighti
                weighti *= 2
                move_x = 0
                weight = 10
            p += 1
    h += move_x
    i += move_y


    for column in range(4, 7):
        p = 0
        weight = 10
        weighti = 10
        move_x = 0
        move_y = 0
        for row in (6, 8 - column, -1):
            movement = state.board.get((row, column - p))
            if movement == state.to_move:
                move_x += 1 * weight
                weight *= 2
                move_y = 0
                weighti = 10
            elif movement == None:
                if movement in state.legal_moves:
                    move_x += 1 * weight / 2
                    move_y += 1 * weighti / 2
                else:
                    move_x += 1 * weight / 3
                    move_y += 1 * weighti / 3
            else:
                move_y += 1 * weighti
                weighti *= 2
                move_x = 0
                weight = 10
            p += 1

    h += move_x
    i += move_y

    return max(h, i)

