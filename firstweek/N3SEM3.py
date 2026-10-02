def nod(a, b):
	if b == 0:
		return a, 1, 0
	d, x1, y1 = nod(b, a % b)
	x = y1
	y = x1 - (a // b) * y1
	return d, x, y
a, b = map(int, input().split())
d, x0, y0 = nod(a, b)
dx = b // d
dy = a // d	
k1 = -x0 // dx
k2 = y0 // dy
start = min(k1, k2) - 2
end = max(k1, k2) + 2	
bestx = 0
besty = 0
sum = 10**18	
for k in range(start, end + 1):
	x = x0 + k * dx
	y = y0 - k * dy
	s = abs(x) + abs(y)
	if s < sum:
		sum = s
		bestx = x
		besty = y
	elif s == sum:
		if x < bestx:
			bestx = x
			besty = y	
print(best_x, best_y, d)
