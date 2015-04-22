
#class HeuristicManager:

    #heuristicCollection = [heuristic, heuristicNew]
    #index = 0


    #def getHeuristic(self):

    #   toGive = self.heuristicCollection[self.index%len(self.heuristicCollection)]
    #    self.heuristicCollection.remove(self.index)


def heuristic(state):
    board = state.board
    h = 0
    for x in range(1,7):
        for y in range(1,8):
            if board.get((x,y)) == state.to_move:
                h += 1
    return h

def heuristicNew(state):
    board = state.board
    h = 0
    for row in range(1,7):
        in_row = 4
        for column in range (1,8):
            if board.get((row,column)) == state.to_move or (board.get((row,column)) == None and board.get((row,column)) in state.legal_moves):
                in_row -= 1
        if in_row < 0:
            h += 1 #Modificable

    #por columnas

    for column in range(1,8):
        in_row = 4
        for row in range (1,7):
            if board.get((row,column)) == state.to_move or (board.get((row,column)) == None and board.get((row,column)) in state.legal_moves):
                in_row -= 1
        if in_row < 0:
            h += 1 #Modificable


    #por diagonales
    for row in range(1,4):
        in_row = 4
        for column in range(1,5):
            if board.get((row,column)) == state.to_move or (board.get((row,column)) == None and board.get((row,column)) in state.legal_moves):
                for p in range (1,4):
                    if board.get((row+p,column+p)) == state.to_move or (board.get((row+p,column+p)) == None and board.get((row+p,column+p))in state.legal_moves):
                        h+=1


    for row in range(1,4):
        in_row = 4
        for column in range(4,8):
            if board.get((row,column)) == state.to_move or (board.get((row,column)) == None and board.get((row,column)) in state.legal_moves):
                for p in range (1,4):
                    if board.get((row+p,column-p)) == state.to_move or (board.get((row+p,column-p)) == None and board.get((row+p,column-p))in state.legal_moves):
                        h+=1

    #return toGive