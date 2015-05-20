def k_in_row(state, move, player, (delta_x, delta_y)):
    board = state.board
    nm = 0
    nb = 0
    w = 0
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if board.get((x, y)) == player:
            nm += 1
            w += 1
        else:
            nb += 1
        x, y = x + delta_x, y + delta_y
        if x > state.row or y > state.column or y < 1:
            break
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if board.get((x, y)) == player:
            nm += 1
            w += 1
        else:
            nb += 1
        x, y = x - delta_x, y - delta_y
        if x < 1 or y < 1 or y > state.column:
            break
    if board.get(move) == player:
        nm -= 1
    if board.get(move) == None:
        nb -= 1
    return (nm * w) + (0.5 * nb)


def heuristic(state):
    if state.utility != 0 and state.to_move == 'X':
        return state.utility
    if state.utility != 0 and state.to_move == 'O':
        return -state.utility
    h = 0

    max_row = state.row
    for move in state.legal_moves:
        if move[0] < max_row:
            max_row = move[0]

    for i in range(max_row, state.row+1):
            h += k_in_row(state, (i, state.k),state.to_move,  (0, 1))
            h += k_in_row(state, (i, state.k),state.to_move,  (1, -1))
            h += k_in_row(state, (i, state.k),state.to_move, (1, 1))
    for j in range(1, state.column+1):
            h += k_in_row(state, (state.k, j),state.to_move, (1, 0))
    return h



def patterns(jugador, lista):
    h = 0
    player = 'O'
    if jugador == 'O':
        player = 'X'

    # print len(lista)
    for i in range(0, len(lista) - 4):

        if lista[i] == jugador and lista[i + 1] == jugador and lista[i + 2] == jugador and lista[i + 3] == None:
            h += 5000
            #return h
            continue
        if lista[i] == jugador and lista[i + 1] == jugador and lista[i + 2] == None and lista[i + 3] == jugador:
            h += 5000
            #return h
            continue
        if lista[i] == jugador and lista[i + 1] == None and lista[i + 2] == jugador and lista[i + 3] == jugador:
            h += 5000
            #return h
            continue
        if lista[i] == None and lista[i + 1] == jugador and lista[i + 2] == jugador and lista[i + 3] == jugador:
            h += 5000
            #return h
            continue

    if h > 0:
        return h

    for i in range(0, len(lista) - 3):
        if lista[i] == jugador and lista[i + 1] == jugador and lista[i + 2] == jugador:
            h += 1000
            #return h
            continue
        if lista[i] == jugador and lista[i + 1] == player and lista[i + 2] == player:
            h += 200
            #return h
            continue
        if lista[i] == player and lista[i + 1] == jugador and lista[i + 2] == player:
            h += 200
            #return h
            continue
        if lista[i] == player and lista[i + 1] == player and lista[i + 2] == jugador:
            h += 200
            #return h
            continue
        if lista[i] == jugador and lista[i + 1] == jugador and lista[i + 2] == None:
            h += 50
            #return h
            continue
        if lista[i] == jugador and lista[i + 1] == None and lista[i + 2] == jugador:
            h += 50
            #return h
            continue
        if lista[i] == None and lista[i + 1] == jugador and lista[i + 2] == jugador:
            h += 50
            #return h
            continue

    if h > 0:
        return h

    for i in range(0, len(lista) - 2):
        if lista[i] == jugador and lista[i + 1] == jugador:
            h += 5
            #return h
            continue
        if lista[i] == jugador and lista[i + 1] == None:
            h += 1
            #return h
            continue
        if lista[i] == None and lista[i + 1] == jugador:
            h += 1
            #return h
            continue

    return h


def lines(state, move, (delta_x, delta_y)):
    board = state.board
    x, y = move
    lista = list()
    while x < 7 and y < 8 and y > 0 and x > 0:
        lista.append(board.get((x, y)))
        x, y = x + delta_x, y + delta_y
    return lista


def sum_heuristics(state):
    if state.utility != 0 and state.to_move == 'X':
        return state.utility
    if state.utility != 0 and state.to_move == 'O':
        return -state.utility


    h = 0

    #crear listas

    lista_de_listas = list()
    for i in range(1, 7):
        lista_de_listas.append(lines(state, (i, 1), (0, 1)))
        lista_de_listas.append(lines(state, (i, 7), (1, -1)))
        lista_de_listas.append(lines(state, (i, 1), (1, 1)))
    for j in range(1, 8):
        lista_de_listas.append(lines(state, (1, j), (1, 0)))

    lista_de_comienzos_de_diagonales = ((6, 2), (6, 3), (6, 4), (6, 5), (6, 6))

    flag = 0
    for comienzo in lista_de_comienzos_de_diagonales:
        if flag <= 2:  # 2 es la mitad de la longitud de la lista creada arriba.
            lista_de_listas.append(lines(state, comienzo, (1, 1)))
        if flag >= 2:
            lista_de_listas.append(lines(state, comienzo, (1, -1)))
        flag += 1

    #llamar a patrones

    for collection in lista_de_listas:
        if len(collection) > 3:
            h += patterns(state.to_move, collection)


    return h