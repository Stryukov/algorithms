def main():
    num_lines = input()
    numbers = num_lines.split(' ')
    parity = []
    for num in numbers:
        if int(num) % 2 == 0:
            parity.append(True)
        else:
            parity.append(False)
    result = 'FAIL'
    if all(elem == parity[0] for elem in parity):
        result = 'WIN'
    print(result, parity)


if __name__ == '__main__':
    main()
