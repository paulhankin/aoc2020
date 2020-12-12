dirs = []
for line in open('day12.txt'):
	line = line.strip()
	if not line:
		continue
	dirs.append((line[0], int(line[1:])))

DIRS = {
	'N': (0, 1),
	'E': (1, 0),
	'S': (0, -1),
	'W': (-1, 0),
}

L = {
	'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'
}
R = {
	'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'
}

def addn(x, y, d, n):
	x += DIRS[d][0] * n
	y += DIRS[d][1] * n
	return x, y

x, y, d = 0, 0, 'E'
for dir, n in dirs:
	if dir == 'L':
		for _ in range((n//90) % 4):
			d = L[d]
	elif dir == 'R':
		for _ in range((n//90) % 4):
			d = R[d]
	elif dir == 'F':
		x, y = addn(x, y, d, n)
	else:
		x, y = addn(x, y, dir, n)

print('part 1', x, y, abs(x) + abs(y))

x, y, wx, wy = 0, 0, 10, 1
for dir, n in dirs:
	if dir == 'L':
		for _ in range((n//90) % 4):
			wx, wy = -wy, wx
	elif dir == 'R':
		for _ in range((n//90) % 4):
			wx, wy = wy, -wx
	elif dir == 'F':
		x += wx * n
		y += wy * n
	else:
		wx, wy = addn(wx, wy, dir, n)

print('part 2', x, y, abs(x) + abs(y))

