"""2. Check word is in dictionary"""

def wordInDictionary(word, dictionary):
	testWord = word
	with open(dictionary, 'r') as f:
		wordList = [line.rstrip('\n') for line in f]

		inDictionary = testWord in wordList

		return inDictionary

