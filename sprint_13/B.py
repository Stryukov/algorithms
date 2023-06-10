def phone_combinations(digits):
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []
    generate_combinations("", digits, letters, result)
    return result


def generate_combinations(current, remaining_digits, letters, combinations):
    if len(remaining_digits) == 0:
        combinations.append(current)
        return

    for letter in letters[remaining_digits[0]]:
        generate_combinations(
            current + letter, remaining_digits[1:], letters, combinations
        )


def main():
    digits = str(input())
    combinations = phone_combinations(digits)
    print(*combinations)


if __name__ == '__main__':
    main()
