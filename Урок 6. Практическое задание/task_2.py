"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
import collections
from pympler import asizeof

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

for i in range(1, 1000): # увеличим размер массива
    array.append(7)

###########################################################################################3
def max_coll():
    counter = collections.Counter(array)
    key_max = counter.most_common()
    return key_max[0][0], key_max[0][1]

print("func_1:", asizeof.asizeof((func_1())))
print("func_2:", asizeof.asizeof((func_2())))
print("max_coll", asizeof.asizeof((max_coll())))

"""
использование Collections не только быстрее - что было выяснено в Lesson 4 / task_4: 
    func_1 14.0197108
    func_2 17.010997
    max_coll 0.5865653000000002

но еще и занимает меньше памяти
func_1: 208
func_2: 208
max_coll 120
"""