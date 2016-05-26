""" Hangman Result Report """
# Modules Required
import re # regex module
import getpass # for hidden input
from string import ascii_lowercase # for quick alphabet
import operator # for getting key from dictionary

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

""" Guess Miss Reduce """
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
def main():
# Runs through the functions in order

	file = 'words2.txt'  # the dictionary file we'll use
	
	# 1. Build the array from the words in the Dictionary File
	dictionary = buildDict(file) 
	with open('hangmanresults.txt', 'w+') as g: # opens file we will write results to
		# Writes Header
		g.write('Input Words, Guessed Letters, Miss Letters, No. Misses\n')
		
		# Loops over ever word in the dictionary file List
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
						
						letter_guess = uModeLetter(dictionary,alphabet)
						
						input_guess = letter_guess

						if input_guess in answer:
							tries += 1
							hits += answer.count(input_guess)
							letters_hit += input_guess

							solution = tryHitReduce(answer,solution,input_guess)

						else:
							tries += 1
							misses += 1
							letters_missed += input_guess
					letters_tried = letters_missed + letters_hit

				# Write to the results: Word, list of letters tried, 
				# letters that were misses, and total misses.	
				g.write('%s,%s,%s,%d\n' % (solution,letters_tried,letters_missed,misses))
			
			else: # Skips word that have '-' in them
				next


main()




