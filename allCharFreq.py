"""6. Analyse for all letters in words in dictionary"""
from string import ascii_lowercase

def allCharFreq(dictionaryList):
	builtDict = dictionaryList
	charFreq = {}
	alphabet = ascii_lowercase

	for a in alphabet:
		charFreq[a] = 0

	for word in builtDict:
		for b in alphabet:
			for w in word:
				if b == w:
					charFreq[b] +=1

	return charFreq

def sumAllCharFreq(dictionary):
	charFreq = dictionary
	total = 0.0

	for c in charFreq:
		total += charFreq[c]

	return total




