def nint(x):
	x = x.strip()
	if x == 'x':
		return None
	return int(x)

data = open('day13.txt').readlines()
ts = int(data[0])
buses = [nint(x) for x in data[1].split(',')]

BTS = None
best_score = None
for b in buses:
	if b is not None:
		bt = -ts % b
		if BTS is None or bt < BTS:
			BTS = bt
			best_score = b * bt
print('part 1', best_score)

def gcde(a, b):
	oldr, r = a, b
	olds, s = 1, 0
	oldt, t = 0, 1
	while r != 0:
		q = oldr // r
		oldr, r = r, oldr - q * r
		olds, s = s, olds - q * s
		oldt, t = t, oldt - q * t
	return oldr, olds, oldt

constraints = [((-i) % b, b) for i, b in enumerate(buses) if b is not None]

while len(constraints) > 1:
	a1, n1 = constraints[-1]
	a2, n2 = constraints[-2]
	g, m1, m2 = gcde(n1, n2)
	assert g == 1
	assert m1*n1 + m2*n2 == 1
	x = a1*m2*n2 + a2*m1*n1
	x = x % (n1 * n2)
	constraints = constraints[:-2]
	constraints.append((x, n1*n2))
sol = constraints[0][0]
print('part 2', int(sol))
