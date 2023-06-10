# Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно понять, является ли первая из них подпоследовательностью второй. Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос, просто посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.

# Формат ввода
# В первой строке записана строка s.

# Во второй —- строка t.

# Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки не могут быть пустыми.

# Формат вывода
# Выведите True, если s является подпоследовательностью t, иначе —– False.

# Пример:
# Ввод
# abc
# ahbgdcu

# Вывод 
# True


def is_sequence(line1, line2):
    i = 0
    j = 0
    while i < len(line1) and j < len(line2):
        if line1[i] == line2[j]:
            i += 1
            j += 1
        else:
            j +=1
    return i == len(line1)


def main():
    line1 = input()
    line2 = input()
    print(is_sequence(line1, line2))


if __name__ == '__main__':
    main()