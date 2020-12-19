def parse_part(p):
	if p.startswith('"'):
		return p[1]
	return [int(x) for x in p.split(' ')]


def parse_rule(x):
	key, rhs = x.split(': ')
	parts = rhs.split(' | ')
	return int(key), [parse_part(p) for p in parts]

def parse_file(f):
	rules = dict()
	data = []
	for line in f:
		line = line.strip()
		if ':' in line:
			key, parts = parse_rule(line)
			rules[key] = parts
		elif line:
			data.append(line)
	return rules, data

def rule_regexp1(rules, r, part2):
	parts = []
	for p in r:
		if type(p) == int:
			parts.append(rule_regexp(rules, p, part2))
		else:
			parts.append(p)
	if len(parts) == 1:
		return parts[0]
	return ''.join('(%s)' % x for x in parts)

def rule_regexp(rules, rn, part2):
	if part2:
		if rn == 8:
			x42 = rule_regexp1(rules, [42], part2)
			return ('(%s)+' % x42)
		elif rn == 11:
			x42 = rule_regexp1(rules, [42], part2)
			x31 = rule_regexp1(rules, [31], part2)
			parts = []
			for i in range(1, 44):
				parts.append('((%s){%d}(%s){%d})' % (x42, i, x31, i))
			return '|'.join(parts)

	parts = [rule_regexp1(rules, p, part2) for p in rules[rn]]
	if len(parts) == 1:
		return parts[0]
	return '|'.join('(%s)' % x for x in parts)


import re

x = open('day19.txt').readlines()
rules, data = parse_file(x)
print(max(len(x) for x in data))
for part in [1, 2]:
	r01 = re.compile('^(%s)$' % rule_regexp(rules, 0, part2=False))
	r0 = re.compile('^(%s)$' % rule_regexp(rules, 0, part2=(part==2)))
	S = 0
	for line in data:
		if r01.match(line) or r0.match(line):
			S += 1
			print(line, 'OK')
		else:
			print(line, 'no')
	print('part', part, S)

