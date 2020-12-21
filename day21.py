data = []

all_ingreds = set()

with open('day21.txt') as f:
	for line in f:
		line = line.strip()
		if not line:
			continue
		left, right = line.split(' (contains ')
		right = right[:-1]
		allergens = right.split(', ')
		ingredients = left.split(' ')
		data.append((ingredients, allergens))
		all_ingreds = all_ingreds | set(ingredients)

amap = dict()
for ingredients, allergens in data:
	for a in allergens:
		if a not in amap:
			amap[a] = set(ingredients)
		else:
			amap[a] = amap[a] & set(ingredients)


mig = set()
for ingreds in amap.values():
	mig = mig | ingreds

never_ingreds = all_ingreds - mig
S = 0
for ing, _ in data:
	for i in ing:
		S += (i in never_ingreds)

def match(amap):
	allergens = set(amap)
	matched = set()
	m = dict()
	while len(matched) < len(allergens):
		for a, i in amap.items():
			if a in m:
				continue
			r = i - matched
			assert len(r) > 0
			if len(r) > 1:
				continue
			r = list(r)[0]
			matched.add(r)
			m[a] = r
			break
		else:
			assert False
	return m


print('part 1', S)
m = match(amap)
p2 = ','.join(m[k] for k in sorted(m))
print('part 2', p2)