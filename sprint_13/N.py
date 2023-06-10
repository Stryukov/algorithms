import sys


# def get_flower_beds(array):
#     if len(array) == 1:
#         return array

#     left = get_flower_beds(array[:len(array)//2])
#     right = get_flower_beds(array[len(array)//2:])

#     result = [None] * len(array)
#     l, r, k = 0, 0, 0
#     while l < len(left) and r < len(right):
#         is_merge = False
#         if left[l] <= right[r]:
#             is_merge = append_flowers_beds(result, left[l], k)
#             l += 1
#         else:
#             is_merge = append_flowers_beds(result, right[r], k)
#             r += 1
#         if not is_merge:
#             k += 1

#     while l < len(left):
#         if not append_flowers_beds(result, left[l], k):
#             k += 1
#         l += 1
#     while r < len(right):
#         if not append_flowers_beds(result, right[r], k):
#             k += 1
#         r += 1

#     return result


# def append_flowers_beds(array, item, index):
#     if len(array) < 1 or array[index - 1][1] < item[0]:
#         array[index] = item
#         return False
#     one = array[-1][0]
#     two = max(array[-1][1], item[1])
#     array.pop(index)
#     array[index] = [one, two]
#     return True


def sort_merge(array):
    if len(array) == 1:
        return array

    left = sort_merge(array[:len(array)//2])
    right = sort_merge(array[len(array)//2:])

    result = [None] * len(array)
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1

    return result


def get_flower_beds(not_sorted_array):
    sort_array = sort_merge(not_sorted_array)
    beds = []
    current_start, current_end = sort_array[0]
    for i in range(1, len(sort_array)):
        start, end = sort_array[i]
        if current_end >= start:
            current_end = max(current_end, end)
        else:
            beds.append([current_start, current_end])
            current_start, current_end = start, end
    beds.append([current_start, current_end])
    return beds


def main():
    count = int(input())
    coordinates = []
    for i in range(count):
        line = sys.stdin.readline().rstrip()
        coordinates.append([int(x) for x in line.split()])
    result = get_flower_beds(coordinates)
    for item in result:
        print(*item)


if __name__ == '__main__':
    main()


# def get_flower_beds(array):
#     if len(array) == 1:
#         return array

#     left = get_flower_beds(array[:len(array)//2])
#     right = get_flower_beds(array[len(array)//2:])

#     result = [None] * len(array)
#     l, r, k = 0, 0, 0
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             result[k] = left[l]
#             l += 1
#         else:
#             result[k] = right[r]
#             r += 1
#         if k > 1:
#             # тут нужно сравнить текущий и предыдущий элемент и слить их если необходимо
#             pass
#         k += 1

#     while l < len(left):
#         result[k] = left[l]
#         l += 1
#         k += 1
#     while r < len(right):
#         result[k] = right[r]
#         r += 1
#         k += 1

#     return result