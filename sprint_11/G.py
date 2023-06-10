def main():
    number = int(input())
    result = ''
    if number == 0:
        result = '0'
    while number > 0:
        result += str(number % 2)
        number = number // 2
    print(result[::-1])


if __name__ == '__main__':
    main()
