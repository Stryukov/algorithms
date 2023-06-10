def get_index(array, elem):
    sep = -1
    for i in range(len(array)):
        if array[i] < array[i - 1]:
            sep = i
            break


def binary_search(array, elem):
    mid = len(array) // 2
    if elem == array[mid]:
        return mid
    if len(array) < 1:
        return -1

    if elem > array[mid]:
        binary_search(array[mid:], elem)
    else:
        binary_search(array[:mid], elem)


def main():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    k = 5
    # print(get_index(arr, k))
    print(binary_search([1, 4, 5, 7, 12], 7))


if __name__ == '__main__':
    main()
