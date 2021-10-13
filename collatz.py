n = int(input())
i = 0
while n != 1:
    if n%2 == 0:
        n = n/2
        i += 1
        continue
    else:
        n = 3*n + 1
        i += 1
        continue
    break
print(i)