"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from random import randint
from memory_profiler import profile


@profile
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

num_1000 = randint(10000000, 100000000)

recursive_reverse(num_1000)

"""
декоратор профилировщика вызывается каждый раз при новой итерации рекурсии
в результате, непонятно - скоолько на самом деле будет затрачено памяти на работу скрипта.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           1   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           1       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           2   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           2       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           3   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           3       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           4   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           4       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           3       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           5   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           5       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           4       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           6   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           6       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           5       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           7   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           7       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           6       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           8   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           8       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           7       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           9   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           9       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           8       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


"""