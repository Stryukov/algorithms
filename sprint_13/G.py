# Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового. После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам. Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового. Помогите Рите справиться с этой задачей.
# Примечание: попробуйте решить задачу за один проход по массиву!
# Формат ввода
# В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000. Во второй строке даётся массив, в котором указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.
# Формат вывода
# Нужно вывести в строку через пробел цвета предметов в правильном порядке.
# Пример 1
# Ввод
# 7
# 0 2 1 2 0 0 1
# Вывод
# 0 0 0 1 1 2 2

def sort_wardrobe(array):
    count_arr = [0, 0, 0]
    result = ''
    for value in array:
        count_arr[value] += 1
    for i in range(3):
        result += str(i) * count_arr[i]
    return result


def main():
    count = input()
    arr = [int(x) for x in input().split()]
    result = sort_wardrobe(arr)
    print(*result)


if __name__ == '__main__':
    main()


# def sort_wardrobe(array):
#     COUNT_COLOR = 3
#     count_arr = [0] * COUNT_COLOR
#     for value in array:
#         count_arr[value] += 1
#     index = 0
#     for i in range(COUNT_COLOR):
#         for count in range(count_arr[i]):
#             array[index] = i
#             index += 1
#     return array