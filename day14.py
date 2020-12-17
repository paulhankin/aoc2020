def read_data(f):	
	data = []
	for line in f:
		line = line.strip()
		if not line:
			continue
		left, right = line.split(' = ')
		if left == 'mask':
			assert len(right) == 36
			ones = int(''.join('01'[x=='1'] for x in right), 2)
			zeros = int(''.join('01'[x=='0'] for x in right), 2)
			data.append(('mask', zeros, ones))
		else:
			n = int(left.split('[')[1][:-1])
			data.append(('mem', n, int(right)))
	return data

with open('day14.txt') as f:
	data = read_data(f)

if 0:
	data = read_data([
		'mask = 000000000000000000000000000000X1001X',
		'mem[42] = 100',
		'mask = 00000000000000000000000000000000X0XX',
		'mem[26] = 1',
	])

import collections
mem = collections.defaultdict(int)

MASK_ZERO = 0
MASK_ONE = 0
for ins in data:
	if ins[0] == 'mask':
		MASK_ZERO, MASK_ONE = ins[1], ins[2]
	else:
		v = ins[2]
		v &= ~MASK_ZERO
		v |= MASK_ONE
		v &= 0xffffffffffffffff
		mem[ins[1]] = v
print('part 1', sum(mem.values()))

def all_x_bits(xs, k):
	if k == len(xs):
		yield 0, 0
		return
	for zx, ox in all_x_bits(xs, k+1):
		b = 1 << xs[k]
		yield zx | b, ox
		yield zx, ox | b

for zx, ox in all_x_bits([0, 2, 3], 0):
	assert zx | ox == 0b1101

mem = collections.defaultdict(int)

MASK_ZERO = 0
MASK_ONE = 0
MASK_X = 0
for ins in data:
	if ins[0] == 'mask':
		MASK_ZERO, MASK_ONE = ins[1], ins[2]
		MASK_X = [i for i in range(36) if ((MASK_ZERO >> i) & 1) == ((MASK_ONE >> i) & 1)]
		if False:
			print('{:036b}'.format(MASK_ZERO))
			print('{:036b}'.format(MASK_ONE))
			print('{:036b}'.format(sum(1<<k for k in MASK_X)))
			print()
	else:
		v = ins[2]
		addr = ins[1]
		for zx, ox in all_x_bits(MASK_X, 0):
			a = addr
			a &= ~zx
			a |= (MASK_ONE | ox)
			a &= 0xffffffffffffffff
			if False:
				print('mem[%d] = %d' % (a, v))
			mem[a] = v
print('part 2', sum(mem.values()))

