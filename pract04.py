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
        coor_str = raw_input("Movimiento columna: ")
        coor = str(coor_str).strip()
        c = int(coor[0])

        state = game.make_move(c, state)
        player = 'X'
    else:
        coor_str = raw_input("Movimiento columna: ")
        coor = str(coor_str).strip()
        c = int(coor[0])

        state = game.make_move(c, state)
        #coor_str = raw_input("Movimiento x,y: ")
        #coor = str(coor_str).strip().split(",")
        #x, y = int(coor[0]), int(coor[1])

        #print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)

        #state = game.make_move((x, y), state)
        #state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
