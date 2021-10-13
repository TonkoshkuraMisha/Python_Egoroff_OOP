N = int(input())

def devisorsList(N):
	divList = [1, N]
	n = 2
	while n < N:
		if N%n == 0:
			divList.append(n)
		n += 1
	return divList

if N >= 2 and len(devisorsList(N)) == 0:
    print('Yes')
else:
    print('No')


print(devisorsList(N))



N = int(input())

def devisorsList(N):
	divList = []
	n = 1
	while n <= N:
		if N%n == 0:
			divList.append(n)
		n += 1
	return divList

print(sum(devisorsList(N)))