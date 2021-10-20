def dec_to_bin(x):
    base = 2

    while x > 0:
        digit = x % base
        print(digit, end='')
        x //= base

