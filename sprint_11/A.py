# https://contest.yandex.ru/contest/23389/problems/
def main():
    num_lines = input()
    a, x, b, c = map(int, num_lines.split(' '))
    result = a * x ** 2 + b * x + c
    print(result)


if __name__ == '__main__':
    main()
