# -*- coding: cp1252 -*-
import games
from utils import *

#Clase Conecta4______________________________________________

class Conecta4(Game):

    def __init__(self,row=6,column=7,k=4):
        update(self,row=row,column=column,k=k)
        moves = [(x, y) for x in range(1, row+1)
                 for y in range(1, column+1)]
        legal_moves = [(7,y) for y in range(1, column+1)]
        self.inicial = Struct(to_move='X', utility=0, board={} moves=moves legal_moves=legal_moves)
        
        
    def legal_moves(self,state):
        return state.legal_moves

    def update_legal_moves(self,state,move):
        #quitar moves de movimientos legales
        #comprobar que la fila de move sea menor o igual a 0
        #añadir el movimiento legal

        next_legal_moves = state.legal_moves.copy()
        next_legal_moves.remove(move)
        next_row = move[0]-1
        if next_row != 0:
            #añade a la nueva lista de movimientos legales una tupla
            #con el moviento legal de la fila superior
             next_legal_moves.append((move[0]-1,move[1]))
        return next_legal_moves

    def make_move(self,move,state):
        if move not in state.moves:
            return state
        if move not in legal_moves(state)
            return state
        board= state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        
        legal_moves = update_legal_moves(state,move)
        return Struct(to_move=if_(state.to_move == 'X', 'O', 'X'),
                      utility=self.compute_utility(board, move, state.to_move),
                      board=board, moves=moves, legal_moves=legal_moves)
        

    def utility(self,state,player):
        if player == 'X':
            return state.utility
        if player == 'O':
            return -state.utility

    def terminal_test(self,state):
         return state.utility != 0 or len(state.moves) == 0

    def display(self,state):
        board = state.board
        for x in range(1, self.h+1):
            for y in range(1, self.v+1):
                print board.get((x, y), '.'),
            print

    def compute_utility(self,board,move,player):

    def k_in_row(self,board,moves,player,(delta_x,delta_y)):

        
