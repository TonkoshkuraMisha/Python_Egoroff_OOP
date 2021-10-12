def sum_two_digits(a, b):
    return a + b


list_fib = [1, 1]
for i in range(1000):
    s = sum_two_digits(list_fib[i], list_fib[i + 1])
    list_fib.append(s)
print(*list_fib, sep='\n')
