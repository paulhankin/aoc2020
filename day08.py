def parse(f):
	for line in f:
		line = line.strip()
		if not line: continue
		a, b = line.split(' ')
		b = int(b)
		yield (a, b)

with open('day08.txt') as f:
	data = list(parse(f))

def run(code):
	acc = 0
	pc = 0
	visited = set()
	while True:
		if pc in visited:
			return False, acc
		if pc == len(code):
			return True, acc
		visited.add(pc)
		ins, n = code[pc]
		if ins == 'nop':
			pc += 1
		elif ins == 'acc':
			acc += n
			pc += 1
		elif ins == 'jmp':
			pc += n
		else:
			assert False, ins

print('part 1', run(data))

def try_run(data, i, new_ins):
	old_ins = data[i]
	data[i] = new_ins
	ok, acc = run(data)
	if ok:
		print('part 2', acc)
	data[i] = old_ins

for i, (ins, n) in enumerate(data):
	if ins == 'nop' and i + n < len(data):
		try_run(data, i, ('jmp', n))
	if ins == 'jmp':
		try_run(data, i, ('nop', n))
