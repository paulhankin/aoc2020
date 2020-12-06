
def read_groups():
	group = set()
	for line in open('day06.txt'):
		line = line.strip()
		if not line:
			yield group
			group = set()
		else:
			group |= set(line)
	if group:
		yield group

def read_groups_all():
	group = None
	for line in open('day06.txt'):
		line = line.strip()
		if not line:
			if group is not None:
				yield group
				group = None
		else:
			if group is not None:
				group &= set(line)
			else:
				group = set(line)
	if group is not None:
		yield group


print('part 1', sum(len(g) for g in read_groups()))
print('part 2', sum(len(g) for g in read_groups_all()))
