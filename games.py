"""Games, or Adversarial Search. (Chapters 6)

"""

from utils import *
import random
import heuristic

def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -infinity
        for (a, s) in game.successors(state):
            v = max(v, min_value(s, alpha, beta, depth+1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = infinity
        for (a, s) in game.successors(state):
            v = min(v, max_value(s, alpha, beta, depth+1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state,depth: depth>d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    action, state = argmax(game.successors(state),
                           lambda ((a, s)): min_value(s, -infinity, infinity, 0))
    return action

#______________________________________________________________________________
# Players for Games

def query_player(game, state):
    "Make a move by querying standard input."
    #game.display(state)
    return num_or_str(raw_input('Your move? '))

def random_player(game, state):
    "A player that chooses a legal move at random."
    return random.choice(game.legal_moves(state))

def alphabeta_player1(game, state):
    return alphabeta_search(state, game,4,None,heuristic.heuristic)

def alphabeta_player2(game, state):
    return alphabeta_search(state, game,4,None,heuristic.heuristicNew)

def play_game(game, *players):
    "Play an n-person, move-alternating game."
    state = game.initial
    while True:
        for player in players:
            move = player(game, state)
            print player, move
            state = game.make_move(move, state)
            if game.terminal_test(state):
                print game.display(state)
                return game.utility(state, 'X')

#______________________________________________________________________________
# Some Sample Games

class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
        abstract

    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        abstract
            
    def utility(self, state, player):
        "Return the value of this final state to player."
        abstract

    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        return not self.legal_moves(state)

    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move

    def display(self, state):
        "Print or otherwise display the state."
        print state

    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]

    def __repr__(self):
        return '<%s>' % self.__class__.__name__


#Clase Conecta4______________________________________________

class Conecta4(Game):

    def __init__(self,row=6,column=7,k=4):
        update(self,row=row,column=column,k=k)
        moves = [(x, y) for x in range(1, row+1)
                 for y in range(1, column+1)]
        legal_moves = [(6,y) for y in range(1, column+1)]
        self.initial = Struct(to_move='X', utility=0, board={}, moves=moves, legal_moves=legal_moves)
        
        
    def legal_moves(self,state):
        return state.legal_moves

    def update_legal_moves(self,state,move):
        next_legal_moves = list(state.legal_moves)
        next_legal_moves.remove(move)
        next_row = move[0]-1
        if next_row != 0:
            next_legal_moves.append((move[0]-1,move[1]))
        return next_legal_moves

    def make_move(self,move,state):
        move = self.complete_move(move,state)
        if move not in state.moves:
            return state
        if move not in state.legal_moves:
            return state
        board= state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        
        legal_moves = self.update_legal_moves(state,move)
        return Struct(to_move=if_(state.to_move == 'X', 'O', 'X'),
                      utility=self.compute_utility(board, move, state.to_move),
                      board=board, moves=moves, legal_moves=legal_moves)
        
    def complete_move(self,imove,state):
        for tuple in state.legal_moves:
            x,y = tuple
            if y == imove:
                return (x,imove)

        return None

    def utility(self,state,player):
        if player == 'X':
            return state.utility
        if player == 'O':
            return -state.utility

    def terminal_test(self,state):
         return state.utility != 0 or len(state.moves) == 0

    def display(self,state):
        board = state.board
        for x in range(1, self.row+1):
            for y in range(1, self.column+1):
                print board.get((x, y), '.'),
            print
        for i in range(1,self.column+1):
            print '-' ,
        print
        for i in range(1,self.column+1):
            print i ,
        print

    def compute_utility(self,board,move,player):
        "If X wins with this move, return 1; if O return -1; else return 0."
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return if_(player == 'X', +1, -1)
        else:
            return 0

    def k_in_row(self,board,move,player,(delta_x,delta_y)):
        "Return true if there is a line through move on board for player."
        x, y = move
        n = 0 # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1 # Because we counted move itself twice
        return n >= self.k
        
    def currentBoard(self):
        return board