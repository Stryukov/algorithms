def main():
    lenght_row = int(input())
    line = input()
    words = [x for x in line.split()]
    counts = [len(x) for x in words]
    max = find_max(counts)
    print(f'{words[max]}\n{counts[max]}')


def find_max(counts):
    max = 0
    index_max = 0
    for i in range(len(counts)):
        if counts[i] > max:
            max = counts[i]
            index_max = i
    return index_max


if __name__ == '__main__':
    main()
