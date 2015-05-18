import games

game = games.Conecta4()
state = game.initial


print "Elije el nivel de dificultad"
print "1 para Facil"
print "2 para Medio"
print "3 para Dificil"
coor_str = raw_input("Nivel: ")
nivel = int(coor_str)

jugadorReal = games.JugadorPorNiveles(1)
jugadorProblema = games.JugadorPorNiveles(3)

player = 'X'


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        move = jugadorReal.juega(game,state)
        state = game.make_move(move[1], state)
        print game.utility(state,player)
        player = 'X'
    else:

        print "Thinking..."
        move = jugadorProblema.juega(game=game,state=state)
        #x, y = move
        state = game.make_move(move, state)
        print game.utility(state,player)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break

