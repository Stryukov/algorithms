def main():
    num1 = input()
    num2 = input()
    buffer = 0
    result = ''
    max_len = max(len(num1), len(num2))
    a = num1.zfill(max_len)
    b = num2.zfill(max_len)
    for i in range(max_len - 1, -1, -1):
        num = int(a[i]) + int(b[i]) + buffer
        if num > 1:
            buffer = 1
            num = 1 if num % 2 == 1 else 0
        else:
            buffer = 0
        result = str(num) + result
    if buffer > 0:
        result = str(buffer) + result
    print(result)


if __name__ == '__main__':
    main()
