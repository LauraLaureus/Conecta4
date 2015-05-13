def neoHeuristic(state):
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
                move_x += weight
                weight *= 4
                move_y = 0
                weighti = 10
            elif movement == None:
                if movement in state.legal_moves:
                    move_x += weight / 2
                    move_y += weighti / 2
                else:
                    move_x += weight / 3
                    move_y += weighti / 3
            else:
                move_y += weighti
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
                move_x += weight
                weight *= 4
                move_y = 0
                weighti = 10
            else:
                move_x = 0
                weight = 10
                move_y += weighti
                weighti *= 2
        h += move_x
        i += move_y

    return h-i

def heuristic(state):
    h=10
    i=5
    nx=0
    nb=0
    no=0
    for row in range (1,7):
        for column in range (1,8):
            movement = state.board.get((row,column))
            if movement == state.to_move:
                nx += 1
            elif movement == None:
                nb += 1
            else:
                no += 1
    total = 6*7

    h*=nx/total
    i*=no/total
    h+=nb/total

    return h-i

