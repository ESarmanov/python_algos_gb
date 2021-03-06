"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""

import random

def v_countdown(v_try, v_num):
    try:
        x_tmp = int(input(f"Осталось попыток: {v_try}. Введите число: "))
    except:
        print("Внимательнее. Нужно вводить число.")
        if v_try !=1:
            v_countdown(v_try-1, v_num)
            return
        else:
            print("Попытки закончились. Вы не угадали.")
            return

    if v_try == 1:
        print("Попытки закончились. Вы не угадали.")
        return

    elif x_tmp > v_num:
        print("Нет, загаданное число меньше введенного")
        v_countdown(v_try-1, v_num)
        return

    elif x_tmp < v_num:
        print("Нет, загаданное число больше введенного")
        v_countdown(v_try-1, v_num)
        return

    elif x_tmp == v_num:
        print(f"Угадали! Загаданное число именно {x_tmp}")
        return

    else:
        v_countdown(v_try - 1, v_num)

v_begin, v_end, try_count=0, 100, 10
x=random.randint(v_begin, v_end)
print(x)
print(f"Загадано число от {v_begin} до {v_end}. У вас {try_count} попыток чтобы его угадать.")
v_countdown(try_count, x)