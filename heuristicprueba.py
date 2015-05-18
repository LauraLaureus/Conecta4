def k_in_row(state, move, player, (delta_x, delta_y)):
    board = state.board
    # player = state.to_move
    nm = 0
    nb = 0
    w = 0
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if x > 6 or y > 7 or y < 1:
            break
        if board.get((x, y)) == player:
            nm += 1
            w += 1
        else:
            nb += 1
        x, y = x + delta_x, y + delta_y
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if x < 1 or y < 1 or y > 7:
            break
        if board.get((x, y)) == player:
            nm += 1
            w += 1
        else:
            nb += 1
        x, y = x - delta_x, y - delta_y
    if board.get(move) == player:
        nm -= 1
    if board.get(move) == None:
        nb -= 1
    return (nm * w) + (0.5 * nb)


def heuristicplayer(state, player):
    h = 0
    for i in range(1, 7):
        h += k_in_row(state, (i, 4), player, (0, 1))
        h += k_in_row(state, (i, 4), player, (1, -1))
        h += k_in_row(state, (i, 4), player, (1, 1))
    for j in range(1, 8):
        h += k_in_row(state, (4, j), player, (1, 0))
    return h


def heuristic(state):
    # hx = heuristicplayer(state,'X')
    #ho = heuristicplayer(state,'O')
    #return max(hx,ho)
    if state.utility != 0:
        return state.utility
    hp = heuristicplayer(state, state.to_move)
    return hp


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


    h = 0  # h+=heuristic(state)

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
        #print len(collection)
        if len(collection) > 3:
            h += patterns(state.to_move, collection)
            #print h
    #if h >= 1008000:
    #    return h*10

    #player = 'O'
    #if state.to_move == 'O':
    #    player = 'X'

    #h_adversario=0
    #for collection in lista_de_listas:
    #    h_adversario += patterns(player,collection)
    #    if h_adversario >=600:
    #        h= h_adversario*(-1)
    #        break


    return h