def find_big_digit(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i
        while j > 0 and comparator(arr[j - 1], elem):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = elem
    return arr


def comparator(arg1, arg2):
    combined1 = arg1 + arg2
    combined2 = arg2 + arg1
    return combined1 < combined2


def main():
    count_digits = int(input())
    arr = input().split()
    print(*find_big_digit(arr), sep='')


if __name__ == '__main__':
    main()
