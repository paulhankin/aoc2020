import collections

dirs = ['w', 'e', 'sw', 'se', 'nw', 'ne']

def step(pos, d):
	if d == 0:
		return (pos[0]-1, pos[1])
	elif d == 1:
		return (pos[0]+1, pos[1])
	elif d == 2:
		return (pos[0]-1+pos[1]%2, pos[1]+1)
	elif d == 3:
		return (pos[0]+pos[1]%2, pos[1]+1)
	elif d == 4:
		return (pos[0]-1+pos[1]%2, pos[1]-1)
	elif d == 5:
		return (pos[0]+pos[1]%2, pos[1]-1)
	else:
		assert False

def life_step(flipped):
	nc = collections.Counter()
	for pos, v in flipped.items():
		if not v:
			continue
		for i in range(6):
			nc[step(pos, i)] += 1
	nf = collections.defaultdict(lambda: False)
	for pos, n in nc.items():
		if flipped[pos]:
			if n == 1 or n == 2:
				nf[pos] = True
		else:
			if n == 2:
				nf[pos] = True
	return nf

def read_data(f):
	for line in f:
		line = line.strip()
		if not line: continue
		ns = 0
		r = []
		for c in line:
			i = 'snwe'.index(c)
			assert i != -1
			if c in 'ns':
				assert ns == 0
				ns = i + 1
			else:
				r.append(ns*2+(i-2))
				ns = 0
		yield r
		got = ''.join(dirs[c] for c in r)
		assert got == line

with open('day24.txt') as f:
	data = list(read_data(f))

flipped = collections.defaultdict(lambda: False)
for row in data:
	pos = (0, 0)
	for c in row:
		pos = step(pos, c)
	flipped[pos] = not flipped[pos]

print('part 1', sum(x for x in flipped.values()))

for day in range(100):
	flipped = life_step(flipped)
print('part 2', sum(x for x in flipped.values()))