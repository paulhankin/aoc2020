def n2020(data, K=2020):
	last = dict()
	lastn, n = None, 0

	for i in range(K):
		if i < len(data):
			n = data[i]
		else:
			if lastn in last:
				n = i-1-last[lastn]
			else:
				n = 0
		if i > 0:
			last[lastn] = i-1
		lastn = n
	return lastn

cases = [
	([0,3,6], 436),
	([1,3,2], 1),
	([2,1,3], 10),
	([1,2,3], 27),
	([2,3,1], 78),
	([3,2,1], 438),
	([3,1,2], 1836),
]
failed = False
for data, want in cases:
	got = n2020(data)
	if got != want:
		print('n2020(%s)=%s, want %s' % (data, got, want))
		failed = True
assert not failed

pdata = [0,14,6,20,1,4]
print('part 1', n2020(pdata))
print('part 2', n2020(pdata, 30000000))