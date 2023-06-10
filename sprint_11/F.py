def main():
    line = input()
    clear_line = ''.join(e for e in line if e.isalnum())
    clear_lower_line = clear_line.lower()
    print(isPalindrome(clear_lower_line))


def isPalindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    main()
