# class HeuristicManager:

#heuristicCollection = [heuristic, heuristicNew]
#index = 0


#def getHeuristic(self):

#   toGive = self.heuristicCollection[self.index%len(self.heuristicCollection)]
#    self.heuristicCollection.remove(self.index)


def heuristic(state):
    board = state.board
    h = 0
    for x in range(1, 7):
        for y in range(1, 8):
            if board.get((x, y)) == state.to_move:
                h += 1
    return h


def heuristicNew(state):
    board = state.board
    h = 0
    for row in range(1, 7):
        in_row = 4
        for column in range(1, 8):
            if board.get((row, column)) == state.to_move or (
                    board.get((row, column)) == None and (row, column) in state.legal_moves):
                in_row -= 1
        if in_row < 0:
            h += 1  #Modificable

    #por columnas

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


#Para la heuristica 3

def dar_h(lista, state):
    h = 0
    for i in range(0, len(lista) - 3):
        x = 4
        for j in range(i, i + 4):
            if lista[j] == state.to_move or lista[j] == None:
                x -= 1
        if x == 0:
            h += 1
    return h


def h_filas(state):
    lista = []
    h = 0
    for row in range(1, 7):
        for column in range(1, 8):
            lista.append(state.board.get((row, column)))
            if (row, column) in state.legal_moves:
                h += 5
        h += dar_h(list(lista), state)
        lista = []
    return h


def h_columnas(state):
    lista = []
    h = 0
    for column in range(1, 8):
        for row in range(1, 7):
            lista.append(state.board.get((row, column)))
            if (row, column) in state.legal_moves:
                h += 5
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
            if (row,column) in state.legal_moves:
                h += 5
            p += 1
        p = 0
        h += dar_h(list(lista), state)
        lista = []
    for row in range(4, 7):
        t += 1
        for column in range(1, 8 - t):
            lista.append(state.board.get((row - p, column + p)))
            if (row,column) in state.legal_moves:
                h += 5
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
            if (row,column) in state.legal_moves:
                h += 5
            p += 1
        p = 0
        t += 1
        h += dar_h(list(lista), state)
        lista = []
    t = 0
    for column in range(2, 5):
        for row in range(7, 1 + t, -1):
            lista.append(state.board.get((row - p, column + p)))
            if (row,column) in state.legal_moves:
                h += 5
            p += 1
        p = 0
        t += 1
        h += dar_h(list(lista), state)
        lista = []
    return h


def heuristicaJessica1(state):
    h = 0
    h += h_filas( state)
    h += h_columnas( state)
    h += h_diagonales1( state)
    h += h_diagonales2( state)
    return h

def heuristicaSimplita(state):
    h = 0
    for tuple in state.legal_moves:
        weight = 10
        if tuple[0] == 6:
            h += 5
            continue
        for row_prima in range(tuple[0],6):
            if state.board.get((row_prima+1,tuple[1])) != state.to_move:
                break
            h+=weight
            weight+=10

    return h

def h_contable(state):
    h = 0
    copy = list(state.legal_moves)
    firsts=(copy[0],copy[1],copy[2])
    for tuple in firsts:
        for row_prima in range(tuple[0]+1,7):
            if state.board.get((row_prima,tuple[1])) == state.to_move:
                h+=1
    seconds=(copy[3],copy[4],copy[5])
    for tuple in seconds:
        for row_prima in range(tuple[0]+1,7):
            if state.board.get((row_prima,tuple[1])) == state.to_move:
                h+=1000
    return h