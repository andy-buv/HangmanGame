""" sandbox 3 """

import re # regex module
import getpass # for hidden input
from string import ascii_lowercase # for quick alphabet
import operator # for getting key from dictionary

""" Build Initial Dictionary """
def buildDict(File): 
	with open(File, 'r') as f:
		initDict = [line.rstrip('\n').lower() for line in f]
		return initDict

""" Input word """
def wordInput():
	answer = getpass.getpass("Please type your word:\n")
	return answer.lower()

""" Check word is in dictionary"""
def wordInDictionary(word, dictionary):
	return word in dictionary

""" Solution Regex """ # will update to change to all lowercase
def solRegex(solution,tried):
	n = len(solution)
	g_reg = [''] * n
	regex = ''
	if len(tried) == 0:
		regex = '[a-z]' * n
	else:
		for i in range(n):
			if solution[i] == ' ':
				g_reg[i] = '[^%s]' % tried
			else:
				g_reg[i] = solution[i]

		regex = ('').join(g_reg)
	return r'%s\Z' % regex

""" Build subDict """
def buildSubDict(dictionary, regex):
	reg = re.compile(regex)
	subDict = []

	for word in dictionary:
		mo = reg.match(word)
		if mo != None:
			subDict.append(word)

	return subDict

""" Mode Letter of Dictionary """
def uModeLetter(dictionary,alphabet):
	lFreq = {}

	for a in alphabet:
		lFreq[a] = 0

	for word in dictionary:
		for b in alphabet:
			if b in word:
				lFreq[b] += 1

	modeLetter = max(lFreq.iteritems(), key = operator.itemgetter(1))[0]
	return modeLetter

""" Guess Hit Reduce """	
def guessHitReduce(answer,guess,hit):
	length = len(answer)
	ansList = list(answer)
	gusList = list(guess)
	

	for i in range(length):
		if ansList[i] == hit:
			gusList[i] = hit
		
	guess = ''.join(gusList)
	return guess

""" Guess Miss Reduce """
def guessMissReduce(dictionary, miss):
	startDict = dictionary
	endDict = []
	remove = miss

	for word in startDict:
		if remove not in word:
			endDict.append(word)

	return endDict

#####
def main():

	file = 'words2.txt'
	

	dictionary = buildDict(file)
	with open('hangmanresults.txt', 'w+') as g:

		g.write('Input Words, Guessed Letters, Miss Letters, No. Misses\n')
		
		for word in dictionary:
			if '-' not in word:
				alphabet = ascii_lowercase
				answer = ''
				solution = ''
				letters_hit = ''
				letters_missed = ''
				letters_tried = ''
				tries = 0
				misses = 0
				hits = 0

				answer = word.lower()
				solution = ' ' * len(answer)

				while solution != answer:
					if letters_tried != '':
						alphabet = re.sub('[%s]' % letters_tried, '', alphabet)
					solution_regex = solRegex(solution,letters_tried)
					
					dictionary = buildSubDict(dictionary,solution_regex)
					if len(dictionary) == 1:
						solution = str(dictionary[0])
					else:
						
						#- print ('Numer of words in sub dictionary = ' + str(len(dictionary)))
						letter_guess = uModeLetter(dictionary,alphabet)
						#- print letter_guess
						
						input_guess = letter_guess

						if input_guess in answer:
							#- print ('Hit! Letter ' + input_guess + ' is in the answer.')
							tries += 1
							hits += answer.count(input_guess)
							letters_hit += input_guess

							solution = guessHitReduce(answer,solution,input_guess)

						else:
							#- print ('Miss! Letter ' + input_guess + ' is not in the answer.')
							tries += 1
							misses += 1
							letters_missed += input_guess
					letters_tried = letters_missed + letters_hit

					
				#- print ('Solved! the answer was %s.\n Letters tried = %d: %s. Number of misses = %d.' % (solution, tries, letters_tried, misses)) 
				g.write('%s,%s,%s,%d\n' % (solution,letters_tried,letters_missed,misses))
			else:
				next


main()




