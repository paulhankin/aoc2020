def parse_range(r):
	left, right = r.split('-')
	return int(left), int(right)

def parse_data(f):
	conds = dict()
	mine = None
	nearby = []
	state = 0

	for line in f:
		line = line.strip()
		if not line:
			continue
		if line == 'your ticket:':
			assert state == 0
			state = 1
			continue
		elif line == 'nearby tickets:':
			assert state == 1
			state = 2
			continue
		if state == 0:
			desc, ranges = line.split(': ')
			ranges = ranges.split(' or ')
			ranges = [parse_range(r) for r in ranges]
			(l1, r1), (l2, r2) = ranges
			s1 = range(l1, r1+1)
			s2 = range(l2, r2+1)

			conds[desc] = (ranges, set(s1) | set(s2))

		elif state == 1:
			mine = [int(x) for x in line.split(',')]
		elif state == 2:
			t = [int(x) for x in line.split(',')]
			nearby.append(t)
	return conds, mine, nearby

with open('day16.txt') as f:
	data = parse_data(f)

conds, mine, nearby = data
S = 0

good_tickets = []
cond_names = sorted(conds)
valid_fields = [set(range(len(cond_names))) for _ in range(len(cond_names))]

for ti, t in enumerate(nearby):
	if ti < 10:
		print('raw', ti, t)
	all_ok = True
	for tf, x in enumerate(t):
		oki = set()
		for i, cn in enumerate(cond_names):
			rs = conds[cn]
			if x in rs[1]:
				oki.add(i)
		if not oki:
			S += x
			all_ok = False
		else:
			valid_fields[tf] &= oki
	if all_ok:
		good_tickets.append(t)
print('part 1', S)

field_assn = [None] * len(cond_names)
assigned = set()
for i in range(len(cond_names)):
	pf = [x for x, v in enumerate(valid_fields) if len(v) == i+1]
	assert len(pf) == 1
	pf = pf[0]
	# valid_fields[pf] is the set of indexes of cond_names
	# that are ok
	vf = set(valid_fields[pf]) - assigned
	assert len(vf) == 1
	vf = vf.pop()
	field_assn[pf] = vf
	assigned.add(vf)

print(field_assn)

for ti, t in enumerate(good_tickets):
	print('check', ti, t)
	for i, x in enumerate(t):
		f = field_assn[i]
		if x not in conds[cond_names[f]][1]:
			assert False, 'bad stuff'


if 1:
	for i in range(len(cond_names)):
		print(cond_names[i], field_assn[i])

print(mine)

P = 1
for i, x in enumerate(mine):
	f = field_assn[i]
	if x not in conds[cond_names[f]][1]:
		assert False, 'bad stuff'
	if not cond_names[f].startswith('departure'):
		continue
	P *= x
print('part 2', P)
