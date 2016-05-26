""" Filter Dictionary """
import re
def filterDictionary(dictionary,regex):
	
	reg = re.compile(regex)
	return list(filter(lambda x: reg.match(x),dictionary))

	
# Builds a Regular Expression to represent the Solution
# For the first use, it will create a regex same length as answer for [a-z]
# After that it will check whether a letter has already been placed in solution
# Then it will exclude that letter and all other tries from the other positions 
def solRegex(solution,tried):
	
	g_reg = [''] * len(solution)
	regex = ''
	if len(tried) == 0:
		regex = '[a-z]' * len(solution)
	else:
		for i in range(len(solution)):
			if solution[i] == ' ':
				g_reg[i] = '[^%s]' % tried
			else:
				g_reg[i] = solution[i]

		regex = ('').join(g_reg)
	return r'%s\Z' % regex


answer = 'cat'
solution = '   '

regex =r'[a-z][a-z][a-z]\Z'

guess = 'e'

new_regex = r'[^e][^e][^e]\Z'

guess = 'a'

solution = ' a '

newer_regex = r'[^ea]a[^ea]\Z'




sol_array = ['g'.' ','a','e',' ','r']

regex_array = ['g', '[^tried]', ]