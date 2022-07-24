# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random


def lottery():
    user_input = 2
    random_number = random.randint(0, 1)
    while user_input != 0 and user_input != 1:
        user_input = int(input('Для жеребьевки выберите число 1 или 0: '))

    if random_number == user_input:
        return user_input
    else:
        return random_number


def the_game(numbers_of_candies: int, bot_info='Нет'):
    pool_candies = numbers_of_candies
    count = 1
    while pool_candies != 0:
        if bot_info == 'Да':
            if count % 2 != 0:
                print(f'----------{count} раунд ----------')
                pool_candies -= int(input('Сколько конфет вы берете: '))
                print(f'Осталось {pool_candies} конфет')
                count += 1
            else:
                print(f'----------{count} раунд ----------')
                bot_candies = bot()
                pool_candies -= bot_candies
                print(f'Бот берет {bot_candies} конфет')
                print(f'Осталось {pool_candies} конфет')
                count += 1

        else:
            print(f'----------{count} раунд ----------')
            pool_candies -= int(input('Сколько конфет вы берете: '))
            print(f'Осталось {pool_candies} конфет')
            count += 1

    if bot_info == "Да" and count % 2 != 0:
        print('Победил бот')
    elif bot_info == "Да" and count % 2 == 0:
        print('Вы победили бота!')
    elif bot_info == "Нет" and count % 2 == 0:
        print('Победил первый игрок!')
    elif bot_info == "Нет" and count % 2 != 0:
        print('Победил второй игрок!')


def bot():
    bot_turn = random.randint(1, 28)
    return bot_turn


print('Игра в конфеты\nПравила:\n1.Первый ход определяется жеребьёвкой ')
print('2.За один ход можно забрать не более чем 28 конфет\n3.Все конфеты оппонента достаются сделавшему последний ход.')
players = input('Вы хотите играть с ботом? Да/Нет: ')
candies = int(input('Сколько конфет на кону: '))

if players == 'Да':
    print('Первым ходит игрок')
    the_game(candies, players)
elif players == 'Нет':
    position = lottery()
    if position == 1:
        print(f'Первым ходит тот кто выбрал {position}')
    else:
        print(f'Первым ходит тот кто выбрал 0')
    the_game(candies, players)


