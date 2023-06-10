# ID: 87188216
from typing import List


def find_nearest_zero(n: int, houses: List[int]) -> List[int]:
    """Возвращает массив расстояний каждого элемента входного массива
    до ближайшего нуля.
    """
    nearest_zero = [n] * n
    for i in range(n):
        if not houses[i]:
            nearest_zero[i] = 0
        else:
            nearest_zero[i] = nearest_zero[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if not houses[i]:
            nearest_zero[i] = 0
        else:
            nearest_zero[i] = min(nearest_zero[i + 1] + 1, nearest_zero[i])
    return nearest_zero


def main() -> None:
    count = int(input())
    line = input()
    houses = [int(x) for x in line.split()]
    nearest_zero = find_nearest_zero(count, houses)
    print(*nearest_zero)


if __name__ == '__main__':
    main()
