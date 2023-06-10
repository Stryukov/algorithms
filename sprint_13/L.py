from typing import List


def purchase_date_calculation(
        saving_history: List, price: int, left: int, right: int
) -> int:
    if right <= left:
        return -1
    mid = (left + right) // 2
    if mid == 0 and price <= saving_history[mid]:
        return mid + 1
    if saving_history[mid - 1] < price <= saving_history[mid]:
        return mid + 1
    if price <= saving_history[mid]:
        return purchase_date_calculation(saving_history, price, left, mid)
    elif price > saving_history[mid]:
        return purchase_date_calculation(saving_history, price, mid + 1, right)


def main():
    days_count = int(input())
    saving_history = [int(day) for day in input().split()]
    price = int(input())
    one_cycle = purchase_date_calculation(saving_history, price, 0, days_count)
    two_cycle = purchase_date_calculation(
        saving_history, price * 2, 0, days_count
    )
    print(one_cycle, two_cycle)


if __name__ == '__main__':
    main()
