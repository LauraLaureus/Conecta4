
def cuentaMisFichas(state):
    if state.utility != 0 and state.to_move == 'X':
        return state.utility
    if state.utility != 0 and state.to_move == 'O':
        return -state.utility

    board = state.board
    h = 0
    for x in range(1, 7):
        for y in range(1, 8):
            if board.get((x, y)) == state.to_move:
                h += 1
    return h


def miraloTodo(state):
    if state.utility != 0 and state.to_move == 'X':
        return state.utility
    if state.utility != 0 and state.to_move == 'O':
        return -state.utility

    board = state.board
    h = 0
    for row in range(1, 7):
        in_row = 4
        for column in range(1, 8):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
        if in_row < 0:
            h += 1  # Modificable

    # por columnas

    for column in range(1, 8):
        in_row = 4
        for row in range(1, 7):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
        if in_row < 0:
            h += 1  #Modificable


    #por diagonales
    for row in range(1, 4):
        in_row = 4
        for column in range(1, 5):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                for p in range(1, 4):
                    if board.get((row + p, column + p)) == state.to_move or (
                                    board.get((row + p, column + p)) == None and board.get(
                                    (row + p, column + p)) in state.legal_moves):
                        h += 1

    for row in range(1, 4):
        in_row = 4
        for column in range(4, 8):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                for p in range(1, 4):
                    if board.get((row + p, column - p)) == state.to_move or (
                                    board.get((row + p, column - p)) == None and board.get(
                                    (row + p, column - p)) in state.legal_moves):
                        h += 1

    return h

def soloSumoCuandoHayCuatroEnRayaEnLaListaQueMePasas(lista, state):
    h = 0
    for i in range(0, len(lista) - 3):
        x = 4
        for j in range(i, i + 4):
            if lista[j] == state.to_move or lista[j] == None:
                x -= 1
        if x == 0:
            h += 1
    return h






def dar_h(lista, state):
    h = 0
    for i in range(0, len(lista) - 3):
        x = 4
        m = 0
        for j in range(i, i + 4):
            if lista[j] == state.to_move or lista[j] == None:
                x -= 1
            if lista[j] == None and lista[j] in state.legal_moves:
                m += 1
        if x == 0:
            h += m * 10
    return h


def h_filas(state):
    lista = []
    h = 0
    for row in range(1, 7):
        for column in range(1, 8):
            lista.append(state.board.get((row, column)))
            #if (row, column) in state.legal_moves:
            #    h += 5
        h += dar_h(list(lista), state)
        lista = []
    return h


def h_columnas(state):
    lista = []
    h = 0
    for column in range(1, 8):
        for row in range(1, 7):
            lista.append(state.board.get((row, column)))
            #if (row, column) in state.legal_moves:
            #    h += 5
        h += dar_h(list(lista), state)
        lista = []
    return h


def h_diagonales1(state):
    lista = []
    h = 0
    t = 0
    p = 0
    for row in range(1, 4):
        for column in range(1, 8 - row):
            lista.append(state.board.get((row + p, column + p)))
            #if (row,column) in state.legal_moves:
            #    h += 5
            p += 1
        p = 0
        h += dar_h(list(lista), state)
        lista = []
    for row in range(4, 7):
        t += 1
        for column in range(1, 8 - t):
            lista.append(state.board.get((row - p, column + p)))
            #if (row,column) in state.legal_moves:
            #    h += 5
            p += 1
        p = 0
        h += dar_h(list(lista), state)
        lista = []
    return h


def h_diagonales2(state):
    lista = []
    h = 0
    t = 0
    p = 0
    for column in range(2, 5):
        for row in range(1, 7 - t):
            lista.append(state.board.get((row + p, column + p)))
            #if (row,column) in state.legal_moves:
            #    h += 5
            p += 1
        p = 0
        t += 1
        h += dar_h(list(lista), state)
        lista = []
    t = 0
    for column in range(2, 5):
        for row in range(7, 1 + t, -1):
            lista.append(state.board.get((row - p, column + p)))
            #if (row,column) in state.legal_moves:
            #    h += 5
            p += 1
        p = 0
        t += 1
        h += dar_h(list(lista), state)
        lista = []
    return h



def heuristicaJessica1(state):
    if state.utility != 0 and state.to_move == 'X':
        return state.utility
    if state.utility != 0 and state.to_move == 'O':
        return -state.utility
    h = 0
    h += h_filas(state)
    h += h_columnas(state)
    h += h_diagonales1(state)
    h += h_diagonales2(state)
    return h




def heuristicElevado4(state):
    board = state.board
    h = 0
    for row in range(1, 7):
        in_row = 4
        for column in range(1, 8):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
                h += 1
            else:
                in_row = 4
                h -= 1
        if in_row <= 0:
            h += 5  #Modificable

    #por columnas

    for column in range(1, 8):
        in_row = 4
        for row in range(1, 7):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
                h += 1
            else:
                in_row = 4
                h -= 1
        if in_row <= 0:
            h += 5  #Modificable


    #por diagonales
    for row in range(1, 4):
        for column in range(1, 5):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                for p in range(1, 4):
                    if board.get((row + p, column + p)) == state.to_move or (
                                    board.get((row + p, column + p)) == None and board.get(
                                    (row + p, column + p)) in state.legal_moves):
                        h += 1
                    else:
                        h -= 1
            else:
                h -= 1

    for row in range(1, 4):
        for column in range(4, 8):
            if board.get((row, column)) == state.to_move or (
                            board.get((row, column)) == None and (row, column) in state.legal_moves):
                for p in range(1, 4):
                    if board.get((row + p, column - p)) == state.to_move or (
                                    board.get((row + p, column - p)) == None and board.get(
                                    (row + p, column - p)) in state.legal_moves):
                        h += 1
                    else:
                        h -= 1
            else:
                h -= 1

    return h




def controladora(state):

    if state.utility !=0 and state.to_move == 'X':
        return state.utility
    elif state.utility != 0 and state.to_move== 'O':
        return  -state.utility

    #Maximo de la fila de movimientos legales
    row = 7
    for tuple in state.legal_moves:
        if tuple[0] < row:
            row = tuple[0]

    h = 0
    i = 0
    for x in range(row, 7):
        weight = 10
        weighti = 10
        for y in range(1, 8):
            movement = state.board.get((x, y))
            if movement == state.to_move:
                h += weight
                weight += 10
            elif movement == None and movement in state.legal_moves:
                h += 5
                i += 5
            else:
                i += weighti
                weighti += 10

    for tuple in state.legal_moves:
        weight = 10
        weighti = 10
        if tuple[0] == 6:
            h += 5
            continue
        for row_prima in range(tuple[0], 6):
            if state.board.get((row_prima + 1, tuple[1])) == state.to_move:
                h += weight
                weight += 10
            else:
                i += weighti
                weighti += 10

    return h - i


def ponderada(state):
    if state.utility !=0 and state.to_move == 'X':
        return state.utility
    elif state.utility != 0 and state.to_move== 'O':
        return  -state.utility

    row = 7
    for tuple in state.legal_moves:
        if tuple[0] < row:
            row = tuple[0]

    h = 0
    i = 0

    for x in range(row, 7):
        weight = 10
        weighti = 10
        move_x = 0
        move_y = 0
        for y in range(1, 8):
            movement = state.board.get((x, y))
            if movement == state.to_move:
                move_x += 1
                move_y = 0
            elif movement == None and movement in state.legal_moves:
                move_x += 1
                move_y += 1
            else:
                move_y += 1
                move_x = 0
        h += weight * move_x
        i += weighti * move_y

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
                move_x += 1
                move_y = 0
            else:
                move_x = 0
                move_y += 1
        h += weight * move_x
        i += weighti * move_y

    return 0.5 * h + 0.5 * i

