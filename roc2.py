def g(x):
	y = 2
	return y+x//y-x

def f(n):
	n //= 2 #4
	if n%2 == 0:
		return n ** 2
	elif n > 100:
		return n%100
	else:
		return g(n-3)

def ct(n):
	a = f(n%10)
	b = n//10
	c = n%100
	if (abs(a-b)//3 + b) < c:
		print(f(a-1))
	else:
		print(g(a//4)+f(a))
	print(f(n+g(c%6)))

print(ct(238))