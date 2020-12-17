import collections

def neighbours(x):
	for i in range(-1, 2):
		for j in range(-1, 2):
			for k in range(-1, 2):
				if i == j == k == 0:
					continue
				yield x[0] + i, x[1] + j, x[2] + k

def neighbours4(x):
	for i in range(-1, 2):
		for j in range(-1, 2):
			for k in range(-1, 2):
				for l in range(-1, 2):
					if i == j == k == l == 0:
						continue
					yield x[0] + i, x[1] + j, x[2] + k, x[3] + l


def life3_step(grid):
	nc = collections.Counter()
	for g in grid:
		for n in neighbours(g):
			nc[n] += 1
	g2 = set()
	for g in grid:
		if nc[g] == 2 or nc[g] == 3:
			g2.add(g)
	for g, i in nc.items():
		if i == 3 and g not in grid:
			g2.add(g)
	return g2

def life3_step4(grid):
	nc = collections.Counter()
	for g in grid:
		for n in neighbours4(g):
			nc[n] += 1
	g2 = set()
	for g in grid:
		if nc[g] == 2 or nc[g] == 3:
			g2.add(g)
	for g, i in nc.items():
		if i == 3 and g not in grid:
			g2.add(g)
	return g2


def parse_grid(g):
	r = set()
	for i, row in enumerate(g):
		for j, v in enumerate(row):
			if v == '#':
				r.add((j, i, 0))
	return r

def parse_grid4(g):
	r = set()
	for i, row in enumerate(g):
		for j, v in enumerate(row):
			if v == '#':
				r.add((j, i, 0, 0))
	return r


def print_grid(grid):
	mins = [1e9, 1e9, 1e9]
	maxs = [-1e9, -1e9, -1e9]
	for g in grid:
		for i in range(3):
			mins[i] = min(mins[i], g[i])
			maxs[i] = max(maxs[i], g[i])
	for z in range(mins[2], maxs[2]+1):
		print('z=%d' % z)
		for y in range(mins[1], maxs[1]+1):
			for x in range(mins[0], maxs[0]+1):
				print('.#'[(x,y,z) in grid], sep='', end='')
			print()
		print()

g = parse_grid([
	'.#.', '..#', '###'
])

g = parse_grid(open('day17.txt'))

print_grid(g)
for c in range(6):
	g = life3_step(g)
	print('after %d steps' % (c+1))
	print_grid(g)
print('part1', sum(1 for _ in g))

g = parse_grid4(open('day17.txt'))

for c in range(6):
	g = life3_step4(g)
print('part2', sum(1 for _ in g))

