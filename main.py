import games
import time

k = None
while k == None or (k != 4 and k != 5 and k!=6):
    print "Cuantas fichas quieres conectar?"
    print "4 para 4"
    print "5 para 5"
    print "6 para 6"
    coor_str = raw_input("Nivel: ")
    k = int(coor_str)


game = games.Conecta4(k=k)
state = game.initial

nivel = None
while nivel == None or (nivel > 3 or nivel <0):
    print "Elije el nivel de dificultad"
    print "1 para Facil"
    print "2 para Medio"
    print "3 para Dificil"
    coor_str = raw_input("Nivel: ")
    nivel = int(coor_str)

advisor = None
while advisor == None or (advisor !=2 and advisor !=1):
    print "Quieres consejero?"
    print "1 si"
    print "2 no"
    coor_str = raw_input("Nivel: ")
    advisor = int(coor_str)


jugadorReal = games.JugadorPorNiveles(0)
jugadorProblema = games.JugadorPorNiveles(nivel)


player = 'X'


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        if  advisor == 1:
            print "Consejero pensando..."
            game.advisor(game,state,nivel)

        move = jugadorReal.juega(game,state)
        state2nd = game.make_move(move, state)
        if state != state2nd:
            state = state2nd
            player = 'X'
    else:
        print "Thinking..."
        move = jugadorProblema.juega(game=game,state=state)
        state = game.make_move(move, state)
        #print game.utility(state,player)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        print "Resultado: ",game.winner
        break

