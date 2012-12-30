from random import randint

def take_turn(pegs, printGame):
    # if there are no remaining pegs, we've won!
    if not pegs: return True

    # roll two dice
    a, b = randint(1,6), randint(1,6)
    
    # check against history string in both possible ways
    try:                high = pegs.index(a+b) + 1
    except ValueError:  high = False
    
    try:                low = pegs.index(a) - pegs.index(b)
    except ValueError:  low = False

    # use the sum if possible, the individual dice if not
    if high:
        pegs.remove(a+b)
        if printGame: print('Rolled a ' + str(a) + ' and a ' + str(b) + ', flipped up peg ' + str(a+b))
        return take_turn(pegs,printGame)
    elif low:
        pegs.remove(a)
        pegs.remove(b)
        if printGame: print('Rolled a ' + str(a) + ' and a ' + str(b) + ', flipped up pegs ' + str(a) + ' and ' + str(b))
        return take_turn(pegs,printGame)
    # if neither is possible, we've lost!
    else:
        if printGame: print('Rolled a ' + str(a) + ' and a ' + str(b) + ', and lost!')
        return False

def play(number_of_games, printGame=False):
    # initialize variables
    games_played = wins = 0
    histogram = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # play as many games as requested
    while games_played < number_of_games:
        # flip pegs back down
        pegs = [1,2,3,4,5,6,7,8,9,10,11,12]
        # start new game
        if printGame: print('---------------- game ' + str(games_played+1) + ' ----------------')
        result = take_turn(pegs, printGame)
        # print final pegs and update histogram based on the number left
        if printGame: print(pegs)
        histogram[len(pegs)] = histogram[len(pegs)] + 1
        # did we win? if so, increment win counter
        if result:
            wins = wins + 1
        # another game completed
        games_played = games_played + 1
    
    # after playing all the games, show the pegs-remaining histogram
    return histogram
