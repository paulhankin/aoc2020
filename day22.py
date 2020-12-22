import collections

def read_data(f):
	p = [[], []]
	n = 1

	for line in f:
		line = line.strip()
		if not line:
			continue
		if '1:' in line:
			n = 0
		elif '2:' in line:
			n = 1
		else:
			p[n].append(int(line))
	return p

with open('day22.txt') as f:
	p1o, p2o = read_data(f)

p1 = collections.deque(p1o)
p2 = collections.deque(p2o)

while p1 and p2:
	c1 = p1.popleft()
	c2 = p2.popleft()
	if c1 > c2:
		p1.append(c1)
		p1.append(c2)
	else:
		p2.append(c2)
		p2.append(c1)

def score(p):
	S = 0
	for i in range(len(p)):
		S += (i+1)*p[-i-1]
	return S
print('part 1', score(p1 or p2))

def RC(p1, p2):
	found = set()
	while p1 and p2:
		key = (tuple(p1), tuple(p2))
		if key in found:
			return 0, p1
		found.add(key)
		c1 = p1.popleft()
		c2 = p2.popleft()
		if c1 <= len(p1) and c2 <= len(p2):
			p1copy = collections.deque(list(p1)[:c1])
			p2copy = collections.deque(list(p2)[:c2])
			winner, _ = RC(p1copy, p2copy)
		else:
			winner = (c2 > c1)
		if winner == 0:
			p1.append(c1)
			p1.append(c2)
		else:
			p2.append(c2)
			p2.append(c1)
	if p1:
		return 0, p1
	else:
		return 1, p2

p1 = collections.deque(p1o)
p2 = collections.deque(p2o)
w, p = RC(p1, p2)
print('part 2', score(p))
