def parse_exp(s, i=0):
	stack = []
	while True:
		if i == len(s):
			assert len(stack) == 1
			return stack[0], i
		if s[i] == '(':
			n, i = parse_exp(s, i+1)
			if len(stack) == 0:
				stack.append(n)
			else:
				left = stack[-2]
				op = stack[-1]
				stack = stack[:-2]
				stack.append((op, left, n))
		elif s[i] == ')':
			assert len(stack) == 1
			return stack[0], i+1
		elif s[i] == ' ':
			i += 1
		elif s[i] in '+*':
			stack.append(s[i])
			i += 1
		elif '0' <= s[i] <= '9':
			n = int(s[i])
			if len(stack) == 0:
				stack.append(n)
			else:
				left = stack[-2]
				op = stack[-1]
				stack = stack[:-2]
				stack.append((op, left, n))
			i += 1
		else:
			assert False

def push_stack(stack, n):
	if len(stack) == 0:
		stack.append(n)
	else:
		if stack[-1] == '+':
			op = stack.pop()
			left = stack.pop()
			stack.append((op, left, n))
		else:
			stack.append(n)

def fold_stack(stack):
	assert len(stack) % 2 == 1
	assert all(stack[i] == '*' for i in range(1, len(stack), 2))
	result = stack[0]
	for i in range(2, len(stack), 2):
		result = ('*', result, stack[i])
	return result


def parse_exp_prec(s, i=0):
	stack = []
	while True:
		if i == len(s):
			return fold_stack(stack), i
		if s[i] == '(':
			n, i = parse_exp_prec(s, i+1)
			push_stack(stack, n)
		elif s[i] == ')':
			return fold_stack(stack), i+1
		elif s[i] == ' ':
			i += 1
		elif s[i] in '+*':
			stack.append(s[i])
			i += 1
		elif '0' <= s[i] <= '9':
			n = int(s[i])
			push_stack(stack, n)
			i += 1
		else:
			assert False

def ev(s):
	if type(s) == int:
		return s
	op, left, right = s
	if op == '+':
		return ev(left) + ev(right)
	elif op == '*':
		return ev(left) * ev(right)
	else:
		assert False, op


egs = [
	('1 + 2 * 3 + 4 * 5 + 6', 71),
	('2 * 3 + (4 * 5)', 26),
	('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
	('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
	('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
]

failed = False
for ex, want in egs:
	p, _ = parse_exp(ex)
	v = ev(p)
	if v != want:
		print('%s = %s = %s, want %s' % (ex, p, v, want))
		failed = True

egs2 = [
	('1 + (2 * 3) + (4 * (5 + 6))', 51),
	('2 * 3 + (4 * 5)', 46),
	('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
	('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
	('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
]
for ex, want in egs2:
	p, _ = parse_exp_prec(ex)
	v = ev(p)
	if v != want:
		print('prec: %s = %s = %s, want %s' % (ex, p, v, want))
		failed = True
assert not failed

S = 0
for line in open('day18.txt'):
	line = line.strip()
	if not line:
		continue
	p, _ = parse_exp(line)
	v = ev(p)
	S += v

print('part 1', S)

S = 0
for line in open('day18.txt'):
	line = line.strip()
	if not line:
		continue
	p, _ = parse_exp_prec(line)
	v = ev(p)
	S += v

print('part 2', S)
