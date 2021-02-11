"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple


def fill_data(count_fabric):
    v_total_revenue = 0
    for i in range(count_fabric):
        while True:
            try:
                v_str = input(
                    f"данные по предприятию {i + 1} (через пробел: Название Прибыль_1кв Прибыль_2кв Прибыль_3кв Прибыль_4кв:")
                v_str_lst = v_str.split()
                fabric = fabrics(v_str_lst[0], int(v_str_lst[1]), int(v_str_lst[2]), int(v_str_lst[3]), int(v_str_lst[4]))
                revenue[fabric.name_fabric] = (fabric.quarter_1 + fabric.quarter_2 + fabric.quarter_3 + fabric.quarter_4) / 4
                v_total_revenue = v_total_revenue + (fabric.quarter_1 + fabric.quarter_2 + fabric.quarter_3 + fabric.quarter_4)
                break
            except:
                print("Внимательнее вводите данные. Должно быть:  Название Прибыль_1кв Прибыль_2кв Прибыль_3кв Прибыль_4кв")

    return (v_total_revenue / count_fabric)


columns = ["name_fabric", "quarter_1", "quarter_2", "quarter_3", "quarter_4"]
fabrics = namedtuple("Fabric", columns)
revenue = {}

while True:
    try:
        n = (int(input("Сколько будет предприятий? >>> ")))
        total_revenue = fill_data(n)
        print(f"Средняя годовая прибыль всех предприятий: {total_revenue}")
        break
    except:
        print("Вводить надо целое число")

fabric_in_avg_rev = [] # список предприятий с прибылью = средней годово1
fabric_lower_avg_rev = [] # список предприятий с прибылью < средней годово1
fabric_upper_avg_rev = [] # список предприятий с прибылью > средней годово1

for key_el, rev_el in revenue.items():
    if rev_el * 4 == total_revenue:
        fabric_in_avg_rev.append(key_el)
    elif rev_el * 4 < total_revenue:
        fabric_lower_avg_rev.append(key_el)
    else:
        fabric_upper_avg_rev.append(key_el)

print()
print(f"предприятия с годовой прибылью равной средней:{fabric_in_avg_rev} ")
print(f"предприятия с годовой прибылью больше средней:{fabric_upper_avg_rev} ")
print(f"предприятия с годовой прибылью меньше средней:{fabric_lower_avg_rev} ")
