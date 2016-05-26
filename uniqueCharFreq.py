"""5. Analyze unique letters in words in dictionary"""
from string import ascii_lowercase

def uniqueCharFreq(dictionaryList):
	builtDict = dictionaryList
	charFreq = {}
	alphabet = ascii_lowercase

	for a in alphabet:
		charFreq[a] = 0

	for word in builtDict:	
		for b in alphabet:
			if b in word:
				charFreq[b] +=1
				
	return charFreq

def sumUniqueCharFreq(dictionary):
	charFreq = dictionary
	total = 0.0

	for c in charFreq:
		total += charFreq[c]

	return total

