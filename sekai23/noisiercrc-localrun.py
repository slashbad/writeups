import secrets
from Crypto.Util.number import *
from Crypto.Cipher import AES
from hashlib import sha256
import json

# from flag import FLAG
FLAG = b"sekai{fakeflag}"

isIrreducible = [True for i in range(1 << 17)]

def init():
	for f in range(2, 1 << 17):
		if isIrreducible[f]:
			ls = [0] # store all multiples of polynomial `f`
			cur_term = f
			while cur_term < (1 << 17):
				ls = ls + [x ^ cur_term for x in ls]
				cur_term <<= 1

			for g in ls[2:]:  # the first two terms are 0, f respectively
				isIrreducible[g] = False

def getCRC16(msg, gen_poly):
	assert (1 << 16) <= gen_poly < (1 << 17)  # check if deg = 16
	msglen = msg.bit_length()

	msg <<= 16
	for i in range(msglen - 1, -1, -1):
		if (msg >> (i + 16)) & 1:
			msg ^= (gen_poly << i)

	return msg

correct_positions = []

def oracle(secret, gen_poly):
	l = int(13.37)
	res = [secrets.randbits(16) for _ in range(l)] 
	correct_position = secrets.randbelow(l)
	res[correct_position] = getCRC16(secret, gen_poly)
	correct_positions.append(correct_position)
	with open("noisiercrc-localrun-leak.json", "w") as f:
		json.dump({
			"secret": secret,
			"correct_positions": correct_positions
		}, f)
	return res


def main():
	init()  # build table of irreducible polynomials

	# key = secrets.randbits(512)
	key = 13243114440536752315667321866358939955217372097602451447776973575077727249709753344173820407833836979236845913059718870554151810605702919398604250233502425
	cipher = AES.new(sha256(long_to_bytes(key)).digest()[:16], AES.MODE_CTR, nonce=b"12345678")
	enc_flag = cipher.encrypt(FLAG)
	print(f"Encrypted flag: {enc_flag.hex()}")

	used = set({})

	for _ in range(int(133.7)):
		gen_poly = int(input("Give me your generator polynomial: "))
		assert (1 << 16) <= gen_poly < (1 << 17)  # check if deg = 16
		if not isIrreducible[gen_poly]:
			print("Invalid polynomial")
			exit(1)

		if gen_poly in used:
			print("No cheating")
			exit(1)

		used.add(gen_poly)

		print(oracle(key, gen_poly))

main()