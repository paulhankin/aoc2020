class Node:
	def __init__(self, i):
		self.val = i
		self.next = None
		self.prev = None

	def insert_after(self, n):
		next = self.next
		self.next = n
		if next:
			next.prev = n
		n.prev = self
		n.next = next

	def remove(self):
		self.next.prev = self.prev
		self.prev.next = self.next
		self.next = None
		self.prev = None
		return self

	def list(self):
		r = []
		cc = self
		while True:
			r.append(cc.val)
			cc = cc.next
			if cc is None or cc is self:
				return r


def step1(cc, maxi, vmap):
	headval = cc.val
	got = []
	gotn = []
	for i in range(3):
		cn = cc.next
		gotn.append(cn)
		got.append(cn.val)
		cn.remove()
	# find value of next current cup
	nc = (headval - 2) % maxi + 1
	while nc in got:
		nc = (nc - 2) % maxi + 1
	dc = cc
	dc = vmap[nc]
	dc.insert_after(gotn[2])
	dc.insert_after(gotn[1])
	dc.insert_after(gotn[0])
	return cc.next

def init(cups, N=0):
	head = Node(cups[0])
	last = None
	vmap = {cups[0]: head}
	if N:
		for i in range(N, len(cups), -1):
			nn = Node(i)
			last = last or nn
			head.insert_after(nn)
			vmap[i] = nn
	for i in range(len(cups)-1, 0, -1):
		nn = Node(cups[i])
		vmap[cups[i]] = nn
		last = last or nn
		head.insert_after(nn)
	# close the loop
	last.next = head
	head.prev = last
	return head, vmap

cc, vmap = init(list(map(int, '643719258')))
# print(cc.list())
M = max(cc.list())
for _ in range(100):
	cc = step1(cc, M, vmap)
cc = vmap[1]
print('part 1', ''.join(str(x) for x in cc.list()[1:]))

cc, vmap = init(list(map(int, '643719258')), 1000000)
# cc, vmap = init(list(map(int, '389125467')), 1000000)
mc = 1000000
for it in range(10*1000*1000):
	cc = step1(cc, mc, vmap)
print()
cc = vmap[1]
print('part 2', cc.next.val * cc.next.next.val)

