# ID: 88133623
from typing import List
import sys


def is_winner(member_one: tuple, member_two: tuple) -> bool:
    """Сравнение данных двух участников конкурса."""
    return set_priority(member_one) > set_priority(member_two)


def set_priority(member: tuple) -> tuple:
    """Подготовка кортежа для компаратора."""
    return (-member[1], member[2], member[0])


def partition(array: List, left: int, right: int) -> int:
    """Смещение элементов массива для быстрой сортировки."""
    pivot = array[right]
    i, j = left, right - 1
    while i <= j:
        while is_winner(pivot, array[i]):
            i += 1
        while is_winner(array[j], pivot):
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    array[i], array[right] = array[right], array[i]
    return i


def quick_sort(array: List, left: int = 0, right: int = None) -> List:
    """Алгоритм быстрой сортировки."""
    if right is None:
        right = len(array) - 1
    if left < right:
        pivot_idx = partition(array, left, right)
        quick_sort(array, left, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, right)
    return array


def main():
    count = int(input())
    arr = []
    for line in range(count):
        line = sys.stdin.readline().rstrip()
        arr_item = tuple(s if not s.isdigit() else int(s) for s in line.split())
        arr.append(arr_item)

    result = quick_sort(arr)
    names = []
    for member in result:
        names.append(member[0])
    print(*names, sep='\n')


if __name__ == '__main__':
    main()
