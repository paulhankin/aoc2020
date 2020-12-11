data = open('day11.txt').read().split('\n')
data = [x.strip() for x in data]
data = [x for x in data if x]

tdata = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split('\n')

def step(data, sc, nebs):
	W = len(data[0])
	H = len(data)
	n = [['.'] * W for _ in range(H)]
	changed = False
	for i in range(W):
		for j in range(H):
			if data[j][i] == '.':
				n[j][i] = '.'
				continue
			ns = sum(data[j2][i2] == '#' for i2, j2 in nebs[i,j])
			if data[j][i] == '#':
				n[j][i] = 'L' if ns >= sc else '#'
			elif data[j][i] == 'L':
				n[j][i] = '#' if ns == 0 else 'L'
			else:
				assert False
			changed = changed or n[j][i] != data[j][i]
	return n, changed

DIRS = [
	(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
]

assert len(set(DIRS)) == 8

def find_nebs(d, i, j, maxk):
	W = len(d[0])
	H = len(d)
	rn = []
	for dx, dy in DIRS:
		for k in range(1, min(maxk+1, max(W, H)+1)):
			i2, j2 = i + dx*k, j + dy*k
			if not (0 <= i2 < W) or not (0 <= j2 < H):
				break
			if d[j2][i2] != '.':
				rn.append((i2, j2))
				break
	return rn

def all_nebs(d, maxk=10000):
	W = len(d[0])
	H = len(d)
	nebs = dict()
	for i in range(W):
		for j in range(H):
			nebs[i, j] = find_nebs(d, i, j, maxk)
	return nebs

odata = data

data = odata
nebs = all_nebs(data, maxk=1)
while True:
	data, changed = step(data, 4, nebs)
	if not changed:
		break
print ('day 1', sum(x=='#' for row in data for x in row))

data = odata
nebs = all_nebs(data)
while True:
	data, changed = step(data, 5, nebs)
	if not changed:
		break
print ('day 2', sum(x=='#' for row in data for x in row))
