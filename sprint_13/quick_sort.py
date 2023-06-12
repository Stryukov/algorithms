from random import choice


def quick_sort2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = choice(arr)
        left = []
        right = []
        for item in arr:
            if item < pivot:
                left.append(item)
            elif item > pivot:
                right.append(item)
        return quick_sort2(left) + [pivot] + quick_sort2(right)


def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort1(left) + [pivot] + quick_sort1(right)


def quick_sort3(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort3(arr, low, pivot_index - 1)
        quick_sort3(arr, pivot_index + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def main():
    arr = [10, 1, 4, 7, 89, 4, 45, 5]
    print(quick_sort3(arr))


if __name__ == '__main__':
    main()
