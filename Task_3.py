# Создайте программу для игры в ""Крестики-нолики"".
import random


def print_bord(desk: list):
    for row in desk:
        print(' '.join([str(i) for i in row]))


def lottery():
    user_input = None
    random_number = random.randint(0, 1)
    while user_input != 0 and user_input != 1:
        user_input = int(input('Для жеребьевки выберите число 1 для игры "x" или 0 для игры "o": '))

    if random_number == user_input:
        return user_input
    else:
        return random_number


def take_cross(number: int, game_bord: list):
    cross = 'x'
    zero = 'o'
    if number == 1 and game_bord[0][0] != zero:
        game_bord[0][0] = cross
        return game_bord
    elif number == 2 and game_bord[0][1] != zero:
        game_bord[0][1] = cross
        return game_bord
    elif number == 3 and game_bord[0][2] != zero:
        game_bord[0][2] = cross
        return game_bord
    elif number == 4 and game_bord[1][0] != zero:
        game_bord[1][0] = cross
        return game_bord
    elif number == 5 and game_bord[1][1] != zero:
        game_bord[1][1] = cross
        return game_bord
    elif number == 6 and game_bord[1][2] != zero:
        game_bord[1][2] = cross
        return game_bord
    elif number == 7 and game_bord[2][0] != zero:
        game_bord[2][0] = cross
        return game_bord
    elif number == 8 and game_bord[2][1] != zero:
        game_bord[2][1] = cross
        return game_bord
    elif number == 9 and game_bord[2][2] != zero:
        game_bord[2][2] = cross
        return game_bord


def take_zero(number: int, game_bord: list):
    cross = 'x'
    zero = 'o'
    if number == 1 and game_bord[0][0] != cross:
        game_bord[0][0] = zero
        return game_bord
    elif number == 2 and game_bord[0][1] != cross:
        game_bord[0][1] = zero
        return game_bord
    elif number == 3 and game_bord[0][2] != cross:
        game_bord[0][2] = zero
        return game_bord
    elif number == 4 and game_bord[1][0] != cross:
        game_bord[1][0] = zero
        return game_bord
    elif number == 5 and game_bord[1][1] != cross:
        game_bord[1][1] = zero
        return game_bord
    elif number == 6 and game_bord[1][2] != cross:
        game_bord[1][2] = zero
        return game_bord
    elif number == 7 and game_bord[2][0] != cross:
        game_bord[2][0] = zero
        return game_bord
    elif number == 8 and game_bord[2][1] != cross:
        game_bord[2][1] = zero
        return game_bord
    elif number == 9 and game_bord[2][2] != cross:
        game_bord[2][2] = zero
        return game_bord


def win_position(cross: bool, zero: bool):
    if cross == True:
        return 1
    elif zero == True:
        return 1
    else:
        return 0


def win_cross(game_bord):
    count = 0
    for i in range(len(game_bord)):
        for j in range(len(game_bord)):
            if count < 3:
                if game_bord[i][j] == 'x':
                    count += 1
            elif j == len(game_bord) - 1:
                count = 0
            else:
                print('Победили крестики')
                return True
    return False


def win_zero(game_bord):
    count = 0
    for i in range(len(game_bord)):
        for j in range(len(game_bord)):
            if count < 3:
                if game_bord[i][j] == 'o':
                    count += 1
            elif j == len(game_bord) - 1:
                count = 0
            else:
                print('Победили нолики')
                return True
    return False


def the_game(user_turn: int):
    board = [['.' for i in range(3)] for j in range(3)]
    print_bord(board)
    count = user_turn
    result = 0

    while result != 1:
        if count % 2 != 0:
            user_turn = int(input('Введите квадрат в который хотите поставить крестик (1-9): '))
            board = take_cross(user_turn, board)
            result = win_position(win_cross(board), win_zero(board))
            print_bord(board)
            count += 1
        elif count % 2 == 0:
            user_turn = int(input('Введите квадрат в который хотите поставить нолик (1-9): '))
            board = take_zero(user_turn, board)
            result = win_position(win_cross(board), win_zero(board))
            print_bord(board)
            count += 1


position = lottery()
if position == 1:
    print('Первые ходят крестики')
else:
    print('Первые ходят нолики')
the_game(position)
