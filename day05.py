data = open('day05.txt').read().split('\n')
data = [x for x in data if x]
print(data)

def seat(s):
	fb = s[:7].replace('F', '0').replace('B', '1')
	lr = s[7:].replace('L', '0').replace('R', '1')
	r, c = int(fb, 2), int(lr, 2)
	sid = r*8 + c
	return r, c, sid

cases = [
	('BFFFBBFRRR', 70, 7, 567),
	('FFFBBBFRRR', 14, 7, 119),
	('BBFFBBFRLL', 102, 4, 820)
]

for s, r, c, sid in cases:
	gr, gc, gid = seat(s)
	if r != gr or c != gc or sid != gid:
		print(s, r, c, sid)
		print('!=', gr, gc, gid)
		assert False

mid = max(seat(s)[2] for s in data)
print('part 1', mid)

got = set(seat(s)[2] for s in data)

for r in range(127):
	for c in range(8):
		sid = r * 8 + c
		if sid not in got and (sid + 1) in got and (sid - 1) in got:
			print('part 2', (r, c), sid)

