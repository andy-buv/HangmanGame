"""Sandbox"""
from string import ascii_lowercase
from collections import OrderedDict



"""1. Enter word as answer"""
def wordInput():
	answer = raw_input("Please type your word:\n")
	return str(answer)


"""2. Check word is in dictionary"""
def wordInDictionary(word, dictionary):
	testWord = word
	with open(dictionary, 'r') as f:
		wordList = [line.rstrip('\n') for line in f]

		inDictionary = testWord in wordList

		return inDictionary


"""3. Get word Length"""
def getWordLength(word):
	length = len(word)
	return length


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


"""5. Analyze unique letters in words in dictionary"""
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


"""6. Analyse for all letters in words in dictionary"""
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


"""7. Make Ordered Dictionary"""
def frequencyOrderedDict(dictionary):
	freqDict = {}
	startDict = dictionary
	finalDict = OrderedDict()
	total = sumUniqueCharFreq(startDict) # taken from 6.

	for s in startDict:
		freqDict[s] = startDict[s]*100/total

	for v in sorted(freqDict, key=freqDict.get, reverse = True):
		finalDict[v] = freqDict[v]

	return finalDict


""" 8. Get top item from ordered Dict """
def getTopGuess(orderedDictionary):
	topGuess = orderedDictionary.items()[0]
	print topGuess
	return topGuess

""" 9.a Letter in Answer """
def letterInAnswer(answer,letter):
	return letter in answer

"""9. Guess Hit Reduce"""
def guessHitReduce(answer,guess,hit):
	length = len(answer)
	ansList = list(answer)
	gusList = list(guess)
	

	for i in range(length):
		if ansList[i] == hit:
			gusList[i] = hit
		
	guess = ''.join(gusList)
	return guess

"""10. If Miss Reduce Dictionary"""

def guessMissReduce(dictionary, miss):
	startDict = dictionary
	endDict = []
	remove = miss

	for word in startDict:
		if remove not in word:
			endDict.append(word)

	return endDict



def main():
	dictionaryFile = "words2.txt" # the file containing the word list
	the_answer = wordInput() # prompt to user to input word
	in_dict = wordInDictionary(the_answer,dictionaryFile) # checks that the word is in the word list file

	if in_dict:
		answer_length = getWordLength(the_answer)
		for i in range(answer_length):
			guess += '.'
		dictionaryBase = buildDictLengthN(dictionaryFile,answer_length)
		uCF = uniqueCharFreq(dictionaryBase)
		aCF = allCharFreq(dictionaryBase)
		uOD = frequencyOrderedDict(uCF)
		aOD = frequencyOrderedDict(aCF)
		uTopGuess = getTopGuess(uOD)
		aTopGuess = getTopGuess(aOD)
		letter = uTopGuess[0]
		if letterInAnswer(the_answer,letter):





	else:
		main()

main()
