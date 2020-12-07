def parse_cond(c):
	x = c.split(' bag')[0]
	n, d = x.split(' ', 1)
	if n == 'no':
		return None
	else:
		return (d, int(n))

def read_data(f):
	for line in f:
		line = line.strip()
		if not line: continue
		first, second = line.split(' contain ')
		conds = second.split(', ')
		first = first.split(' bags')[0]
		conds = [parse_cond(c) for c in conds]
		conds = [c for c in conds if c is not None]
		yield first, conds

with open('day07.txt') as f:
	data = dict(read_data(f))

def contains_bag(x, bag):
	if x == bag:
		return True
	return any(contains_bag(y[0], bag) for y in data[x])

def bag_size(x):
	return 1 + sum(n * bag_size(c) for c, n in data[x])

S = 0
for d in data:
	if d != 'shiny gold':
		S += contains_bag(d, 'shiny gold')
print('part 1', S)

print('part 2', bag_size('shiny gold') - 1)
