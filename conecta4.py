import games
from utils import *

#Clase Conecta4______________________________________________

class Conecta4(Game):

    def __init__(self,filas=6,columnas=7,fichas=4):
        update(self,filas=filas,columna=columnas,fichas=fichas)
        movimientos = [(x, y) for x in range(1, filas+1)
                 for y in range(1, columnas+1)]
        self.inicial = Struct(to_move='X', utility=0, board={} moves=movimientos)
        
        
    def legal_moves(self,state):
        

    def make_move(self,move,state):
        if move not in state.moves:
            return state
        board= state.board.copy()
        #TODO: comprobar que la lista asociada a board[move] es menor que 6.
        board[move].append(state.to_move)

    def utility(self,state,player):

    def terminal_test(self,state):

    def display(self,state):

    def compute_utility(self,board,move,player):

    def k_in_row(self,board,moves,player,(delta_x,delta_y)):

        
