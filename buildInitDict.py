""" Build Initial Dictionary """

def buildDict(File):
	with open(File, 'r') as f:
		initDict = [line.rstrip('\n') for line in f]

		return initDict

