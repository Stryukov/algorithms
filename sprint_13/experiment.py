def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1')


# gen_binary(2, '')

def decart(s1, s2):
    return [a + b for a in s1 for b in s2]

# print(decart('ab', 'cd'))

# [(a, b, a1, b1) for a in A
#                     for b in B
#                         for a1 in A
#                             for b1 in B]

# abc
# def
