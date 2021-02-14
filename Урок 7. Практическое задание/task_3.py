"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from random import randint
from statistics import median


def fill_lst_not_ord(max_size):
    for i in range(max_size):
        lst_not_ord.append(randint(0, 50))
    return

def mediana(var_list):
    if len(var_list)==1:
        return var_list[0] # если список из 1 элемента, то он и будет медианой
    i = len(var_list) // 2
    for n in range(i):
        var_list.remove(max(var_list))
    return max(var_list)

max_size=11 # должно быть нечетное число
lst_not_ord = []
fill_lst_not_ord(max_size)
ord_lst=lst_not_ord.copy()

print("изначальный список:           ", lst_not_ord)
print("найденная медиана:            ",  mediana(ord_lst[:]))
print("медиана из модуля statistics: ", median(lst_not_ord))


