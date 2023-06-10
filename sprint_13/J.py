def bubble_sotr(arr):
    is_sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        print(*arr)
        return

    swaps = True
    while swaps:
        swaps = False
        for i in range(len(arr) - 1):
            elem = arr[i]
            if elem > arr[i + 1]:
                arr[i] = arr[i + 1]
                arr[i + 1] = elem
                swaps = True
        if swaps:
            print(*arr)


def main():
    len_arr = int(input())
    arr = [int(x) for x in input().split()]
    bubble_sotr(arr)


if __name__ == '__main__':
    main()
