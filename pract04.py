import games
#import conecta4

#game = games.TicTacToe()
#print games.play_game(game, games.random_player, games.alphabeta_player)

game = games.Conecta4()
state = game.initial


player = 'X'

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        #coor_str = raw_input("Movimiento columna: ")
        #coor = str(coor_str).strip()
        #c = int(coor[0])

        move = games.alphabeta_player6(game,state)
        x,y = move
        state = game.make_move(y,state)
        #state = game.make_move(c, state)
        player = 'X'
    else:
        #------------JUGADOR REAL-----------------------
        coor_str = raw_input("Movimiento columna: ")
        coor = str(coor_str).strip()
        c = int(coor[0])
        state = game.make_move(c, state)


        print "Thinking..."
        #-------------JUGADOR ALEATORIO-----------------
        #move = games.random_player(game,state)

        #--------------JUGADOR AlphaBeta


        #move = games.alphabeta_player1(game=game,state=state)

        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)

        #x,y = move
        #state = game.make_move(y,state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break

