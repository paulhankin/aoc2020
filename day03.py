data = [x for x in open('day03.txt').read().split('\n') if x]
H = len(data)
W = len(data[0])

T = 0
for y in range(H):
	x = (y * 3) % W
	T += data[y][x] == '#'
print(T)

P = 1
T = 0

for slope in [1,3,5,7]:
	T = 0
	for y in range(H):
		x = (y * slope) % W
		T += data[y][x] == '#'
	P *= T

T = 0
for y in range(0, H, 2):
	x = (y // 2) % W
	T += data[y][x] == '#'
P *= T

print(P)

