import collections
import math

filename = 'day20.txt'

def read_data(f):
	tn = None
	tile = []
	for line in f:
		line = line.strip()
		if ':' in line:
			if tn is not None:
				yield tn, tile
				tn = None
				tile = []
			tn = int(line[:-1].split(' ')[1])
			continue
		if line:
			tile.append(line)
	if tn is not None:
		yield tn, tile

def get_side(t, i, j, di, dj):
	n = len(t)
	i *= n-1
	j *= n-1
	r = ''
	for k in range(n):
		r += t[j+dj*k][i+di*k]
	return r

def rotate90(tile):
	n = len(tile)
	r = [[None] * n for _ in range(n)]
	for j in range(n):
		for i in range(n):
			r[j][i] = tile[i][n-1-j]
	return r

def flip(tile):
	n = len(tile)
	r = [[None] * n for _ in range(n)]
	for j in range(n):
		for i in range(n):
			r[j][i] = tile[j][n-1-i]
	return r

def tile_rotations(tile):
	for _ in range(2):
		for _ in range(4):
			yield tile
			tile = rotate90(tile)
		tile = flip(tile)

def get_sides(tile):
	r = []
	for t in tile_rotations(tile):
		r.append((
			get_side(t, 0, 0, 1, 0),  # top
			get_side(t, 1, 0, 0, 1),  # right
			get_side(t, 0, 1, 1, 0),  # bottom
			get_side(t, 0, 0, 0, 1),  # left
		))
	return r

with open(filename) as f:
	tiles = dict(read_data(f))

tile_sides = dict()
rots = dict()

for tn, tile in tiles.items():
	tile_sides[tn] = get_sides(tile)
	rots[tn] = list(tile_rotations(tile))

side_map = collections.defaultdict(list)
side_count = collections.defaultdict(int)
for tn, sides in tile_sides.items():
	ss = set()
	for i, s4 in enumerate(sides):
		for j, x in enumerate(s4):
			side_map[(x, j)].append((tn, i))
			ss.add(x)
	for x in ss:
		side_count[x] += 1

nc = 0
S = 1
one_corner = None
found_corners = set()
for tn in tiles:
	corner = True
	for ts in tile_sides[tn]:
		c = sum(side_count[s] == 1 for s in ts) == 2
		corner = corner and c
	if corner:
		one_corner = tn
		nc += 1
		found_corners.add(tn)
		S *= tn

assert nc == 4
print('part 1', S, 'corners', sorted(found_corners))

N = int(math.sqrt(len(tiles)) + 0.1)
assert N * N == len(tiles)

grid = [[None] * N for _ in range(N)]

def find_tile(side, placed, i):
	got = [x for x in side_map[side, i] if x[0] not in placed]
	if not got:
		return None
	assert len(got) == 1
	return got[0]
	
def try_complete(grid, start):
	grid[0][0] = start
	N = len(grid)
	placed = set()
	placed.add(start[0])
	for j in range(N):
		for i in range(N):
			if i == 0 and j == 0:
				continue
			if i > 0:
				tl, rl = grid[j][i-1]
				side = tile_sides[tl][rl][1]
				ft = find_tile(side, placed, 3)
				if ft is None:
					return False
				grid[j][i] = ft
				placed.add(ft[0])
			else:
				tu, ru = grid[j-1][i]
				side = tile_sides[tu][ru][2]
				ft = find_tile(side, placed, 0)
				if ft is None:
					return False
				grid[j][i] = ft
				placed.add(ft[0])
	return True

def ascii_grid(grid):
	tl = rots[grid[0][0][0]][grid[0][0][1]]
	ts = len(tl)
	N = len(grid)
	gs = (ts - 2) * N
	result = [[None] * gs for _ in range(gs)]
	for j in range(gs):
		for i in range(gs):
			ti = i // (ts - 2)
			tj = j // (ts - 2)
			g, gr = grid[tj][ti]
			g = rots[g][gr]
			result[j][i] = g[j % (ts - 2) + 1][i % (ts - 2) + 1]
	return [''.join(row) for row in result]

MONSTER = [
	'                  # ',
	'#    ##    ##    ###',
	' #  #  #  #  #  #   '
]

MONSTER = set((i, j) for j in range(3) for i, c in enumerate(MONSTER[j]) if c == '#')
print(MONSTER)

def monster_at(ag, i, j):
	for mi, mj in MONSTER:
		if ag[j+mj][i+mi] != '#':
			return False
	return True

def count_monsters(ag):
	N = len(ag)
	M = 0
	hashes = sum(x == '#' for row in ag for x in row)
	monster_hashes = set()
	for j in range(N - 2):
		for i in range(N - 19):
			if monster_at(ag, i, j):
				M += 1
	return M, hashes - len(MONSTER) * M



for r in range(8):
	print('trying', r)
	if not try_complete(grid, (one_corner, r)):
		continue
	corners = [grid[0][0], grid[-1][0], grid[0][-1], grid[-1][-1]]
	corners = [x[0] for x in corners]
	print('corners', corners)
	ag = ascii_grid(grid)
	for ag2 in tile_rotations(ag):
		monsters, hashes = count_monsters(ag2)
		if monsters:
			print('part 2', hashes)
			break
	break
