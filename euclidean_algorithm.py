# first variant euclidean algorithm (slow)
a, b = map(int, input().split())
while a != b:
	if a > b:
		a = a - b
	else:
		b = b - a
print(a)

# second variant euclidean algorithm (fast)
a, b = map(int, input().split())
while b > 0:
	#c = a%b
	#a = b
	#b = c
	a, b = b, a%b
print(a)

# very important information
# a * b = НОК * НОД