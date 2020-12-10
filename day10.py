data = open('day10.txt').readlines()
data = [int(x.strip()) for x in data if x.strip()]

data.sort()

data = [0] + data + [data[-1]+3]

ONES = 0
THREES = 0
for i, d in enumerate(data):
	J = data[i-1]
	if d-J == 1:
		ONES += 1
	elif d-J == 3:
		THREES += 1
	J = d
print('part 1', ONES, THREES, ONES * THREES)

W = [1] + [0] * (len(data) - 1)
for i in range(1, len(W)):
	for k in range(1, 4):
		if i-k >= 0 and 0 < data[i] - data[i-k] < 4:
			W[i] += W[i-k]
		# print(i, k, data[i], data[i-k], W[i])

print('part 2', W[-1])
