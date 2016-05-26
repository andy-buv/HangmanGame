""" letter Frequency """
from string import ascii_lowercase
import operator
def uModeLetter(dictionary):
	alphabet = ascii_lowercase
	lFreq = {}

	for a in alphabet:
		lFreq[a] = 0

	for word in dictionary:
		for b in alphabet:
			if b in word:
				lFreq[b] += 1

	modeLetter = max(lFreq.iteritems(), key = operator.itemgetter(1))[0]
	return modeLetter

