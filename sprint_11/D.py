def main():
    days = int(input())
    line = input()
    temp = [int(x) for x in line.split()]
    if len(temp) == 1:
        return 1
    result = chaotic_weather(days, temp)
    return result


def chaotic_weather(days, temp):
    chaos = 0
    for day in range(days):
        if day == 0:
            if temp[day] > temp[day + 1]:
                chaos += 1
        elif day == days - 1:
            if temp[day] > temp[day - 1]:
                chaos += 1
        elif (temp[day] > temp[day - 1]) and (temp[day] > temp[day + 1]):
            chaos += 1
    return chaos


if __name__ == '__main__':
    print(main())
