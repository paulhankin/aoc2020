# test
pub_door = 17807724
pub_card = 5764801

# prod
pub_door = 1965712
pub_card = 19072108

N=20201227

def crack(key, N=N):
	subj = 7
	x = 1
	for i in range(N):
		if x == key:
			return i
		x = (x * subj) % N
	assert False

door_loops = crack(pub_door)
card_loops = crack(pub_card)

enc_key1 = pow(pub_door, card_loops, N)
enc_key2 = pow(pub_card, door_loops, N)

print(enc_key1, enc_key2)
