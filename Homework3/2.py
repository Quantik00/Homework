def div(n):
	divs = []
	i = 2
	while i < int(n ** 0.5) + 1:
		if n % i == 0:
			n //= i
			divs.append(i)
			i -= 1
		i += 1

	if n > 1: 
		divs.append(n)
		
	return divs

n = int(input())
print(div(n))