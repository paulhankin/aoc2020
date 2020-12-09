def read_data(f):
	for line in f:
		line = line.strip()
		if not line: continue
		yield int(line)

with open('day09.txt') as f:
	data = list(read_data(f))

from collections import Counter

test1 = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

def part1(s, N):
	preamble = Counter()
	for i in range(len(s)):
		if len(preamble) == N:
			for p in preamble:
				if s[i] - p in preamble:
					break
			else:
				yield s[i]
		preamble[s[i]] += 1
		if len(preamble) > N:
			if preamble[s[i-N]] == 1:
				del preamble[s[i-N]]
			else:
				preamble[s[i-N]] -= 1

print('should be 127: ', list(part1(test1, 5)))
B, = list(part1(data, 25))
print('part 1', B)

# dataS[i] is the sum of data[0:i]
dataS = [0] * (len(data) + 1)
for i, d in enumerate(data):
	dataS[i+1] = dataS[i] + d
dataD = dict()
for i, d in enumerate(dataS):
	dataD[d] = i

for i in range(1, len(data)+1):
	w = dataS[i] - B
	if w in dataD:
		j = dataD[w]
		if i - j > 2:
			print('part 2', j, i-1)
			m = min(data[j:i])
			M = max(data[j:i])
			print(B, '==', sum(data[k] for k in range(j, i)))
			print('part 2 weakness:', m+M)

