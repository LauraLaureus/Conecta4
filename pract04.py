import games
# import conecta4

#game = games.TicTacToe()
#print games.play_game(game, games.random_player, games.alphabeta_player)

game = games.Conecta4()
state = game.initial

listWinners = []
player = 'X'

for i in range(0, 1):
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            #move = games.random_player(game,state)
            #coor_str = raw_input("Movimiento columna: ")
            #coor = str(coor_str).strip()
            #c = int(coor[0])

            move = games.alphabeta_player16(game, state)
            x, y = move
            state = game.make_move(y, state)
            #state = game.make_move(c, state)
            player = 'X'
        else:
            #------------JUGADOR REAL-----------------------
            #coor_str = raw_input("Movimiento columna: ")
            #coor = str(coor_str).strip()
            #c = int(coor[0])
            #state = game.make_move(c, state)


            print "Thinking..."
            #-------------JUGADOR ALEATORIO-----------------
            #move = games.random_player(game, state)

            #--------------JUGADOR AlphaBeta


            move = games.alphabeta_player16(game=game,state=state)

            #move = games.minimax_decision(state, game)
            #move = games.alphabeta_full_search(state, game)

            x, y = move
            state = game.make_move(y, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            listWinners.append(game.winner)
            game.display(state)
            print "Final de la partida"
            break

    game = games.Conecta4()
    state = game.initial
    player = 'X'

x = 0
o = 0
t = 0
for y in range(0, 1):
    if listWinners[y] == 'X':
        x += 1
    elif listWinners[y] == 'O':
        o += 1
    else:
        t += 1
print 'X:', x, '/5'
print 'O:', o, '/5'
print 'T:', t, '/5'