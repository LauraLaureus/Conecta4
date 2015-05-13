

def vecinoUnitario(state,current):

    vecinos=[]
    if current[1] >= 1 and current[1] < 7:
        neighbour = state.board.get((current[0],current[1]+1))
        if neighbour != None:
            vecinos.append(neighbour)
        neighbour =  state.board.get((current[0]-1,current[1]+1))
        if neighbour != None:
            vecinos.append(neighbour)

    if current[1] <=7 and current[1] > 1:
        neighbour = state.board.get((current[0],current[1]-1))
        if neighbour != None:
            vecinos.append(neighbour)

        neighbour = state.board.get((current[0]-1,current[1]-1))
        if neighbour != None:
            vecinos.append(neighbour)

    if current[0] < 6 and current[0]>=1 :
        vecinos.append(state.board.get((current[0]+1,current[1])))
        neighbour = state.board.get((current[0]+1,current[1]-1))
        if neighbour != None:
            vecinos.append(neighbour)
        neighbour = state.board.get((current[0]+1,current[1]+1))
        if neighbour != None:
            vecinos.append(neighbour)

    return vecinos

def heuristic(state):
    #buscar vecinos de movimientos legales

    h=50
    i=50
    comunidadDeVecinos = []
    for legal_mov in state.legal_moves:
        vecinos = vecinoUnitario(state,legal_mov)
        comunidadDeVecinos.extend(vecinos)
    #contar enemigos
    amigos = comunidadDeVecinos.count(state.to_move)
    total = len(comunidadDeVecinos)

    h*=amigos/total+1
    i*=(total-amigos)/total+1


    return max(h,i)/min(h,i)


