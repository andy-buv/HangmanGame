"""4. Build Dictionary from word length"""

def buildDictLengthN(dictionary, n):
	wordLength = n
	file = dictionary
	builtDict = []
	with open(file, 'r') as f:
		wordList = [line.rstrip('\n') for line in f]

		for word in wordList:
			if len(word) == n:
				builtDict.append(word)

	return builtDict


