from typing import List


def count_freq(s: str) -> List[int]:
	"""
	:return: An array of length 26, containing the frequency
	of each character in the given string.
	"""
	freq = [0] * 26
	for c in s:
		freq[ord(c) - ord("a")] += 1
	return freq


with open("blocks.in") as read:
	n = int(read.readline())
	words = [read.readline().split() for _ in range(n)]

max_blocks = [0] * 26
for w1, w2 in words:
	freq1, freq2 = count_freq(w1), count_freq(w2)
	for c in range(26):
		max_blocks[c] += max(freq1[c], freq2[c])

with open("blocks.out", "w") as written:
	for i in max_blocks:
		print(i, file=written)