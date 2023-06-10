# https://contest.yandex.ru/contest/23758/problems/?nc=6O0V4KlF
import sys


def main():
    num_rows = int(input())
    num_columns = int(input())
    matrix = []
    transposed_matrix = [[]] * num_columns
    for num_row in range(num_rows):
        line = sys.stdin.readline().rstrip()
        matrix_row = [x for x in line.split()]
        matrix.append(matrix_row)

    for new_row in range(num_columns):
        transposed_matrix_row = []
        for row in matrix:
            transposed_matrix_row.append(row[new_row])
        transposed_matrix[new_row] = transposed_matrix_row

    for row in transposed_matrix:
        print(*row)


if __name__ == '__main__':
    main()
