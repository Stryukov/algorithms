# ID: 87188281
from typing import List


def deft_hands(fingers: int, buttons: List[str]) -> int:
    """Считает сколько клавиш можно нажать
    заданным количеством пальцев.
    """
    count_buttons = [0] * 10
    result = 0
    for row in buttons:
        for button in row:
            if button == '.':
                continue
            count_buttons[int(button)] += 1
    for number in count_buttons:
        if 0 < number <= fingers * 2:
            result += 1
    return result


def main():
    fingers = int(input())
    buttons = [input() for row in range(4)]
    wins = deft_hands(fingers, buttons)
    print(wins)


if __name__ == '__main__':
    main()
