# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random


def lottery():
    user_input = 2
    random_number = random.randint(0, 1)
    while user_input != 0 and user_input != 1:
        user_input = int(input('Для жеребьевки выберите число 1 или 0: '))

    if random_number == user_input:
        print(f'Первым ходит тот кто выбрал {user_input}')
    else:
        print(f'Первым ходит тот кто выбрал {random_number}')


def the_game(numbers_of_candies: int):
    pool_candies = numbers_of_candies
    count = 1
    while pool_candies != 0:
        print(f'----------{count} раунд ----------')
        pool_candies -= int(input('Сколько конфет вы берете: '))
        print(f'Осталось {pool_candies} конфет')
        count += 1
    print('Вы победили!')


print('Игра в конфеты\nПравила:\n1.Первый ход определяется жеребьёвкой ')
print('2.За один ход можно забрать не более чем 28 конфет\n3.Все конфеты оппонента достаются сделавшему последний ход.')
candies = int(input('Сколько конфет на кону: '))
lottery()
the_game(candies)
