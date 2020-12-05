import re

pat = re.compile('([0-9]+)-([0-9]+) ([a-z]): (.*)')

def format_line(s):
	m = pat.match(s)
	if m is None:
		print('invalid "%s"' % s)
		assert False
	lim0 = int(m[1])
	lim1 = int(m[2])
	c = m[3]
	pw = m[4]
	return lim0, lim1, c, pw

def valid(x):
	lim0, lim1, c, pw = x
	return lim0 <= pw.count(c) <= lim1

def valid2(x):
	lim0, lim1, c, pw = x
	return (pw[lim0-1] == c) + (pw[lim1-1] == c) == 1

data = open('day2.txt').read().split('\n')
data = [format_line(x) for x in data if x]

print(sum(valid2(x) for x in data))