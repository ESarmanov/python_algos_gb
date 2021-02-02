"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def operation(result):
    oper = str(
        input(f"На текущий момент результат равен: {result}. Ждем следующего действия (+ - * /). 0 - для выхода>>>"))
    if oper == "+":
        try:
            num = input_num()
            result = def_sum(result, num)
            operation(result)
        except:
            operation(result)

    elif oper == "-":
        try:
            num = input_num()
            result = def_sum(result, -num)
            operation(result)
        except:
            operation(result)

    elif oper == "*":
        try:
            num = input_num()
            result = def_multiply(result, num)
            operation(result)
        except:
            operation(result)

    elif oper == "/":
        try:
            num = input_num()
            if num != 0:
                result = def_multiply(result, 1 / num)
                operation(result)
            else:
                print("На 0 делить нельзя!")
                operation(result)
        except:
            operation(result)

    elif oper == "0":
        print("------------------------------------------------")
        return ()

    else:
        print(f"Поддерживаемые операции только: + - * /")
        operation(result)

    return result


def input_num():
    try:
        num = int(input("a?>>>"))
    except:
        print("вводить надо число")
        num = None
    return num


def def_sum(result, num):
    result = result + num
    return result


def def_multiply(result, num):
    result = result * num
    return result


result = 0
#num = 0
print("рекурсивный калькулятор. 0 - конец цикла")
print(f"Конечный езультат составил {operation(result)}")
