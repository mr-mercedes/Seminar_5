# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coder(user_input: str):
    code_str = ''
    count = 1
    for i in range(1, len(user_input)):
        if user_input[i] == user_input[i - 1]:
            count += 1
        elif user_input[i] != user_input[i - 1]:
            code_str += str(count) + user_input[i - 1]
            count = 1
    if user_input[-1] != user_input[-2]:
        count = 1
        code_str += str(count) + user_input[-1]
    else:
        code_str += str(count) + user_input[-1]
    return code_str


def decoder(coder_string: str):
    coding_list = ''
    point = 0
    for i in range(len(coder_string)):
        if coder_string[i].isalpha():
            coding_list += coder_string[point:i+1] + ' '
            point = i+1

    coding_list = [str(i) for i in coding_list.split()]
    count = 0
    tmp = ''
    result = ''
    for item in coding_list:
        if len(item) > 2:
            while item[count].isdigit():
                tmp += item[count]
                count += 1
            else:
                result += int(tmp) * item[len(item) - 1]
                count = 0
                tmp = ''
        else:
            result += int(item[0]) * item[1]
            count = 0
            tmp = ''

    return result


user_string = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'


print(f'Закодированный текст [{user_string}] через алгоритм RLE --->[{coder(user_string)}]<---')

if input('Хотите декодировать текст? Да/Нет: ').lower() == 'да':
    print(f'Раскодированный текст RLE --->[{decoder(coder(user_string))}] ')
elif input('Хотите раскодировать свой RLE код? Да/Нет: ').lower() == 'да':
    print(decoder(input('Введите RLE код: ')))
else:
    print('Нет так нет')


