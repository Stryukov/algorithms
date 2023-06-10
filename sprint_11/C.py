import sys


def main():
    rows_matrix = int(input())
    columns_matrix = int(input())
    matrix = []
    for row in range(rows_matrix):
        line = sys.stdin.readline().rstrip()
        matrix_row = [int(x) for x in line.split()]
        matrix.append(matrix_row)
    y = int(input())
    x = int(input())
    neighbors = search_neighbor(matrix, x, y, rows_matrix, columns_matrix)
    print(' '.join(map(str, neighbors)))


def search_neighbor(matrix, x, y, max_row, max_col):
    neighbrs = []
    if y < max_row - 1:
        neighbrs.append(matrix[y + 1][x])
    if x < max_col - 1:
        neighbrs.append(matrix[y][x + 1])
    if y > 0:
        neighbrs.append(matrix[y - 1][x])
    if x > 0:
        neighbrs.append(matrix[y][x - 1])
    neighbrs.sort()
    return neighbrs


if __name__ == '__main__':
    main()
