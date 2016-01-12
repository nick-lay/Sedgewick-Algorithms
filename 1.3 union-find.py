#!/usr/bin/env python3
"""
"""


def quickfind(pair):
    """Реализация простого алгоритма, решающего задачу связности. В основе
    алгоритма лежит использование массива целых чисел, обладающего тем
    свойством, что p и q связаны тогда и только тогда, когда p-ая и q-ая записи
    массива равны.
    Инициализируем i-ую запись массива значением i. Чтобы реализовать операцию
    union для p и q, мы просматриваем массив, изменяя все записи с именем p на
    записи с именем q.

    Arguments:
        pair {list} -- [лист пар вершин]

    Returns:
        [dict] -- [словарь вершин]
    """
    result = dict()
    for p, q in pair:
        result[p] = p
        result[q] = q
    for p, q in pair:
        t = result[p]
        if t == result[q]:
            continue
        for k in result:
            if result[k] == t:
                result[k] = result[q]
    return result


def quickunion(pair):
    """Решение задачи связности методом быстрого объединения.
    Тоже что quickfind, но выполняет меньше вычислений для объединения за счет
    выполнения большего количества вычислений для поиска

    Arguments:
        pair {list} -- [лист пар вершин]

    Returns:
        [dict] -- [словарь вершин]
    """
    result = dict()
    for p, q in pair:
        result[p] = p
        result[q] = q
    for p, q in pair:
        while p != result[p]:
            p = result[p]
        while q != result[q]:
            q = result[q]
        if p == q:
            continue
        result[p] = q
    return result


def weightedquickunion(pair):
    """Модификация quickunion. В служебных целях для каждого объекта, заводим
    дополнительный массив, представляющий собой массив количества узлов в
    соответствующем дереве, чтобы операция объединения могла связать меньшее
    из двух указанных деревьев с большим, тем самым предотвращая разрастание
    длинных путей в деревьях

    Arguments:
        pair {list} -- [лист пар вершин]

    Returns:
        [dict] -- [словарь вершин]
    """
    result = dict()
    sz = dict()
    for p, q in pair:
        sz[p] = 1
        sz[q] = 1
        result[q] = q
        result[p] = p
    for p, q in pair:
        while p != result[p]:
            p = result[p]
        while q != result[q]:
            q = result[q]
        if p == q:
            continue
        if sz[p] < sz[q]:
            result[p] = q
            sz[q] += sz[p]
        else:
            result[q] = p
            sz[p] += sz[q]
    return result


pair = ((3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (2, 9),
        (5, 9), (7, 3), (4, 8), (5, 6), (0, 2), (6, 1))
# print(quickfind(pair))
# print(quickunion(pair))
print(weightedquickunion(pair))

# pair = ((0, 2), (1, 4), (2, 5), (3, 6), (0, 4), (6, 0), (1, 3))
# print(quickfind(pair))
# print(quickunion(pair))
