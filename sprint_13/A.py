# https://contest.yandex.ru/contest/24734/problems/H/
def check_bracket_seq(seq):
    stack = []
    for bracket in seq:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


def bracket_generator(n, prefix):
    if n == 0:
        if check_bracket_seq(prefix):
            print(prefix)
    else:
        bracket_generator(n - 1, prefix + '(')
        bracket_generator(n - 1, prefix + ')')


def main():
    n = int(input())
    bracket_generator(n * 2, '')


if __name__ == '__main__':
    main()
