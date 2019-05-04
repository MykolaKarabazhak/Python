from functools import reduce


# Задание 1. Встроенные типы данных, операторы, функции и генераторы
#
# Напишите реализации объявленных ниже функций. Для проверки
# корректности реализации ваших функций, запустите тесты:
#
# pytest test_homework01.py
#
# Если написанный вами код не содержит синтаксических ошибок,
# вы увидите результаты тестов ваших решений.


def fac(n):
    """
    Факториал

    Факториал числа N - произведение всех целых чисел от 1 до N
    включительно. Например, факториал числа 5 - произведение
    чисел 1, 2, 3, 4, 5.

    Функция должна вернуть факториал аргумента, числа n.
    """
    if n == 1:
        return n
    else:
        res = 1
        for i in range(1, n+ 1):
            res = i * res


    # if n == 1:
    #     return 1
    # else:
    #     return n * fac(n - 1)

from operator import  mul
def fact_reduice(n):
    return reduce(lambda x,y:x * y , range(1,n),n)
    #return reduce((mul(,range(1,n),n)

def gcd(a, b):
    """
    Наибольший общий делитель (НОД) для двух целых чисел.

    Предполагаем, что оба аргумента - положительные числа
    Один из самых простых способов вычесления НОД - метод Эвклида,
    согласно которому

    1. НОД(a, 0) = a
    2. НОД(a, b) = НОД(b, a mod b)

    (mod - операция взятия остатка от деления, в python - оператор '%')
    """
    #return a if b == 0 else gcd( b, a %b) # решение рекурсией для не нормального\
                                           # человека попробуйте !!!!!!
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    c = a + b


def fib():
    """
    Генератор для ряда Фибоначчи

    Вам необходимо сгенерировать бесконечный ряд чисел Фибоначчи,
    в котором каждый последующий элемент ряда является суммой двух
    предыдущих. Начало последовательности: 1, 1, 2, 3, 5, 8, 13, ..

    Подсказка по реализации: для бесконечного цикла используйте идиому

    while True:
      ..

    """
    x = 1
    y = 1
    res = 0
    while True:
        res = x + y
        x = y
        y = x


def Fib_():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b



def flatten(seq):
    """
    Функция,
преобразующая вложенные последовательности любого уровня
    вложенности в плоские, одноуровневые.
    >>> flatten([])
    []
    >>> flatten([1, 2])
    [1, 2]
    >>> flatten([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten([(1, 2), (3, 4)])
    [1, 2, 3, 4]
    """
    flat_list = []
    for i in seq:
        if isinstance(i,tuple) or isinstance(i,list):
            flat_list.extend(flatten(i))
        else:
            flat_list.append()
    return  flat_list



from collections.abc import Iterable
def flat(seq):
    acc = []
    for x in seq:
        if type(x) in {list,tuple}:
        acc.extend(flat(x))
        else:
            acc.append(x)

def gelatteen(seq):
    for i in seq:
        if type(i) in {list,tuple}:
            yield from gelatteen(i)
        else:
            yield i