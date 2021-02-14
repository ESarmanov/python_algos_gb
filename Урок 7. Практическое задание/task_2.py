"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit


def fill_lst_not_ord(max_size):
    for i in range(max_size):
        lst_not_ord.append(uniform(0, 50))
    return


def merge(v_left, v_right):
    merge_lst = []
    i = 0
    j = 0
    while i < len(v_left) and j < len(v_right):
        if v_left[i] <= v_right[j]:
            merge_lst.append(v_left[i])
            i += 1
        else:
            merge_lst.append(v_right[j])
            j += 1
    merge_lst += v_left[i:] + v_right[j:]
    return merge_lst


def merge_sort(v_lst):
    if len(v_lst) <= 1:
        return v_lst
    else:
        left_arr = v_lst[:len(v_lst) // 2]
        right_arr = v_lst[len(v_lst) // 2:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))


max_size = int(input("введите количество элемeнтов массива: "))
lst_not_ord = []  # оргинальный не отсортированный список
fill_lst_not_ord(max_size)

ord_list = merge_sort(lst_not_ord)

print(lst_not_ord)
print(ord_list)

print("-------------------- замеры ------------------------------------------")
print(timeit('merge_sort(lst_not_ord)', setup='from __main__ import merge_sort, lst_not_ord', number=10000))

"""
max_size = 10
-------------------- замеры ------------------------------------------
0.43118410000000007

max_size = 100
-------------------- замеры ------------------------------------------
7.1816354

max_size = 1000
-------------------- замеры ------------------------------------------
83.11970360000001

"""
