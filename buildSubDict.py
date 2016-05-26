""" Build subDict """
import re
def buildSubDict(dictionary, regex):
	
	reg = re.compile(regex)
	print reg
	subDict = []

	for word in dictionary:
		mo = reg.match(word)
		if mo != None:
			subDict.append(word)

	return subDict
		
