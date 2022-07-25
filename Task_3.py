# Создайте программу для игры в ""Крестики-нолики"".
import random


def print_bord(desk: list):
    print("-" * 13)
    for i in range(3):
        print("|", desk[0 + i * 3], "|", desk[1 + i * 3], "|", desk[2 + i * 3], "|")
        print("-" * 13)


def lottery():
    user_input = None
    random_number = random.randint(0, 1)
    while user_input != 0 and user_input != 1:
        user_input = int(input('Для жеребьевки выберите число 1 для игры "X" или 0 для игры "O": '))

    if random_number == user_input:
        return user_input
    else:
        return random_number


def take_input(player_token: str):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(game_board: list):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if game_board[each[0]] == game_board[each[1]] == game_board[each[2]]:
            return game_board[each[0]]
    return False


def the_game(game_board):
    position = lottery()
    counter = position
    if position == 1:
        print('Первые ходят крестики')
    else:
        print('Первые ходят нолики')
    win = False
    while not win:
        print_bord(game_board)
        if counter % 2 != 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4 - position:
            tmp = check_win(game_board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter - position == 9:
            print("Ничья!")
            break
    print_bord(game_board)


board = list(range(1, 10))
the_game(board)
input("Нажмите Enter для выхода!")
