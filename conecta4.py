import games
from utils import *

#Clase Conecta4______________________________________________

class Conecta4(Game):

    def __init__(self,filas=6,columnas=7,fichas=4):
        update(self,filas=filas,columna=columnas,fichas=fichas)
        self.tablero = [range(numero_columnas) for i in range(numero_filas)]
        
    def legal_moves(self,state):

    def make_move(self,move,state):

    def utility(self,state,player):

    def terminal_test(self,state):

    def display(self,state):

    def compute_utility(self,board,move,player):

    def k_in_row(self,board,moves,player,(delta_x,delta_y)):

        
