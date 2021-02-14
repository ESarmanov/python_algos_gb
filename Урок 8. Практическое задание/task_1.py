"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def haffman_encode(v_str):
    v_lst = []
    for el, freq_el in Counter(v_str).items():
        v_lst.append((freq_el, len(v_lst), Leaf(el)))
    heapq.heapify(v_lst)
    count = len(v_lst)
    while len(v_lst) > 1:
        freq_left, _count_left, left = heapq.heappop(v_lst)
        freq_rigth, _count_right, right = heapq.heappop(v_lst)
        heapq.heappush(v_lst, (freq_left + freq_rigth, count, Node(left, right)))
        count += 1
    code = {}
    if v_lst:
        [(_freq, count, root)] = v_lst
        root.walk(code, "")
    return code


def main_s(v_str):
    code = haffman_encode(v_str)
    encoded = " ".join(code[ch] for ch in v_str)
    return encoded


str_to_code = "beep boop beer!"

print(f"{str_to_code} = {main_s(str_to_code)}")
