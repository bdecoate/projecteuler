def brute_force_it(cipher):
	letter_range = range(ord('A'), ord('z'))
	for i in letter_range:
		for j in letter_range:
			for k in letter_range:
				message = []
				for c in range(0, len(cipher), 3):
					try:
						letter1 = chr(cipher[c] ^ i)
						message.append(letter1)
						letter2 = chr(cipher[c + 1] ^ j)
						message.append(letter2)
						letter3 = chr(cipher[c + 2] ^ k)
						message.append(letter3)
					except IndexError:  # skip letters outside ascii range
						continue

				# found word 'beginning' using brute force and grep
				str_message = "".join(message)
				if str_message.find('beginning') >= 0:
					return map(ord, str_message)


with open('p059_cipher.txt', 'r') as cipher_file:
	cipher = map(int, cipher_file.read().split(','))


val = brute_force_it(cipher)
print sum(val)
