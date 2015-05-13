def k_in_row(state,move,(delta_x, delta_y)):
        board = state.board
        player = state.to_move
        nm=0
        nb=0
        x,y = move
        while board.get((x,y)) == player or board.get((x,y)) == None:
                if x>6 or y>7 or y<1:
                        break
                if board.get((x,y)) == player:
                        nm+=1
                else:
                        nb+=1
                x, y = x+dellta_x, y+delta_y
        x,y = move
        while board.get((x,y)) == player or board.get((x,y)) == None:
                if x<1 or y<1 or y>7:


                        break
                if board.get((x,y)) == player:
                        nm+=1
                else:
                        nb+=1
                x, y = x-dellta_x, y-delta_y
        if board.get(move) == player:
                nm -=1
        if board.get(move) == None:
                nb -=1
        return nm+(0,5*nb)

def heuristic(state):
        h=0
        for i in range (1,7):
                h+=k_in_row(state,(i,4),(0,1))
                h+=k_in_row(state,(i,4),(1,-1))
                h+=k_in_row(state,(i,4),(1,1))
        for j in range (1,8):
                h+=k_in_row(state,(4,j),(1,0))
        return h