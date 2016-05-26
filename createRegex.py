""" Create Regex guess"""

def createRegex(word):
	length = len(word)
	regex = r'[a-zA-Z][a-z]{%d}\Z' % (length - 1)
	return regex



