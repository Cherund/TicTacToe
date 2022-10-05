def start_the_game():
    for i in range(9):
        if len(s) == 9:
            s[i] = ' '
        else:
            s.append(' ')
    print('Welcome to the Tic Tac Toe game')
    print(f'Here is a field:')
    tictac_field()
    print('You can choose in which square you want to put your X or O from 1 to 9')
    player1()


def tictac_field():
    field = f' {s[0]} | {s[1]} | {s[2]} \n' \
            f'-----------\n' \
            f' {s[3]} | {s[4]} | {s[5]} \n' \
            f'-----------\n' \
            f' {s[6]} | {s[7]} | {s[8]} \n'
    print(field)


def player1():
    print('Player 1 move.')
    chosen_square = int(input('Choose a number in what square you want to put your mark: '))

    if s[chosen_square - 1] == 'X' or s[chosen_square - 1] == 'O':
        print('That square is already taken. Try another one.')
        player1()
    elif chosen_square > 9:
        print('That square do not exist. Try one more time')
        player1()
    else:
        s[chosen_square - 1] = 'X'

    tictac_field()

    if game_is_on():
        player2()
    else:
        another_round()


def player2():
    print('Player 2 move.')
    chosen_square = int(input('Choose a number in what square you want to put your mark: '))
    if s[chosen_square - 1] == 'X' or s[chosen_square - 1] == 'O':
        print('That square is already taken. Try another one.')
        player2()
    elif chosen_square > 9:
        print('That square do not exist. Try one more time')
        player2()
    else:
        s[chosen_square - 1] = 'O'

    tictac_field()

    if game_is_on():
        player1()
    else:
        another_round()


def game_is_on():
    if s[0] == s[1] == s[2] and s[0] != ' ':
        identify_winner(s[0])
        return False
    elif s[0] == s[3] == s[6] and s[0] != ' ':
        identify_winner(s[0])
        return False
    elif s[0] == s[4] == s[8] and s[0] != ' ':
        identify_winner(s[0])
        return False
    elif s[1] == s[4] == s[7] and s[1] != ' ':
        identify_winner(s[1])
        return False
    elif s[2] == s[4] == s[6] and s[2] != ' ':
        identify_winner(s[2])
        return False
    elif s[2] == s[5] == s[8] and s[2] != ' ':
        identify_winner(s[2])
        return False
    elif s[3] == s[4] == s[5] and s[3] != ' ':
        identify_winner(s[3])
        return False
    elif s[6] == s[7] == s[8] and s[6] != ' ':
        identify_winner(s[6])
        return False

    for mark in s:
        if mark == ' ':
            return True

    print('It is a tie!')
    return False


def identify_winner(winners_mark):
    if winners_mark == 'X':
        print(' Player 1 won!')
    elif winners_mark == 'O':
        print('Player 2 won!')


def another_round():
    print('Want to play another round?')
    answer = input('Print Y for Yes and N for No ').upper()
    if answer == 'Y':
        start_the_game()
    elif answer == 'N':
        print('Have a good day! Bye!')
    else:
        print("I don't get it. Let's try one more time")
        another_round()


s = []
start_the_game()
