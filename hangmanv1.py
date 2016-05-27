"""Hangman Terminal"""
# Modules Required
import re
import getpass
from string import ascii_lowercase
import operator
from collections import OrderedDict
""" Build Initial Dictionary """ 
# Creates the list of words from the file
def buildDict(File):
	with open(File, 'r') as f: # opens file
		initDict = [line.rstrip('\n').lower() for line in f] 

	return initDict

""" Input word """ 
# Uses getpass to keep the input hidden
# User inputs their word for the program to guess
# returns String
def wordInput():
	answer = getpass.getpass("Please type your word:\n")

	return answer.lower()

""" Check word is in dictionary"""
# Checks that the input word is in the dictionary file we are using
# Returns Boolean
def wordInDictionary(word, dictionary):

	return word in dictionary

""" Solution Regex """ 
# Builds a Regular Expression to represent the Solution
# For the first use, it will create a regex same length as answer for [a-z]
# After that it will check whether a letter has already been placed in solution
# Then it will exclude that letter and all other tries from the other positions 
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
# Creates a sub-dictionary from words matching a regular expression
def buildSubDict(dictionary, regex):
	reg = re.compile(regex)
	subDict = []

	for word in dictionary:
		mo = reg.match(word)
		if mo != None:
			subDict.append(word)

	return subDict

""" Mode Letter of Dictionary """
# Returns the letter that occurs in the most words
# However if there are more than one with the same highest value,
# it returns the first alphabetically.
def uModeLetter(dictionary,alphabet):
	lFreq = {}

	for a in alphabet:
		lFreq[a] = 0

	for word in dictionary:
		for b in alphabet:
			if b in word:
				lFreq[b] += 1


	#print OrderedDict(sorted(lFreq.items(), key = lambda t: t[1], reverse = True))
	modeLetter = max(lFreq.iteritems(), key = operator.itemgetter(1))[0]
	return modeLetter

""" Try Hit Reduce """	
# Rewrites the solution to include the letter found by a correct guess
def tryHitReduce(answer,solution,hit):
	length = len(answer)
	ansList = list(answer)
	solList = list(solution)
	

	for i in range(length):
		if ansList[i] == hit:
			solList[i] = hit
		
	solution = ''.join(solList)
	return solution

""" Try Miss Reduce """
# ??? No longer need this function?
def guessMissReduce(dictionary, miss):
	startDict = dictionary
	endDict = []
	remove = miss

	for word in startDict:
		if remove not in word:
			endDict.append(word)

	return endDict

#####
""" Main Function """
# Runs through the functions in order
def main():
	file = 'words2.txt' # the dictionary file we'll use
	dictionary = buildDict(file)
	
	for word in dictionary:
		valid_word = False
		alphabet = ascii_lowercase # represents the lowercase alphabet
		answer = '' 
		solution = ''
		try_hit = ''
		try_missed = ''
		letters_tried = ''
		tries = 0
		misses = 0
		hits = 0
		
		# 1. Build the array from the words in the Dictionary File
		sub_dictionary = dictionary

		# 2. Get users input for the word to guess, check that it is in the dictionary file
		"""
		while(not valid_word):
			answer = wordInput()
			valid_word = wordInDictionary(answer, dictionary)
		"""
		answer = word
		# 3. Initialize our solution the same length as answer 
		solution = ' ' * len(answer)

		# 4. Start the guessing process
		while solution != answer:
			if letters_tried != '':
				alphabet = re.sub('[%s]' % letters_tried, '', alphabet)
			solution_regex = solRegex(solution,letters_tried)
			
			sub_dictionary = buildSubDict(sub_dictionary,solution_regex)
			#print sub_dictionary
			if len(sub_dictionary) == 1:
				solution = str(sub_dictionary[0])
			else:
				#print ('Numer of words in sub_dictionary = ' + str(len(sub_dictionary)))
				letter_guess = uModeLetter(sub_dictionary,alphabet)
				#print letter_guess
				input_guess = letter_guess#raw_input('Enter your guess Letter: ')

				if input_guess in answer:
				#	print ('Hit! Letter ' + input_guess + ' is in the answer.')
					tries += 1
					hits += answer.count(input_guess)
					try_hit += input_guess

					solution = tryHitReduce(answer,solution,input_guess)

				else:
				#	print ('Miss! Letter ' + input_guess + ' is not in the answer.')
					tries += 1
					misses += 1
					try_missed += input_guess
			letters_tried += input_guess

			
		print ('Solved! the answer was %s.\n Letters tried = %d: %s. Number of misses = %d.' % (solution, tries, letters_tried, misses)) 



main()




