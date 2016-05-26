"""7. Make Ordered Dictionary"""
from collections import OrderedDict
def frequencyOrderedDict(dictionary):
	freqDict = {}
	startDict = dictionary
	finalDict = OrderedDict()
	total = sumAllCharFreq(startDict) # taken from 6.

	for s in startDict:
		freqDict[s] = startDict[s]*100/total

	for v in sorted(freqDict, key=freqDict.get, reverse = True):
		finalDict[v] = freqDict[v]

	return finalDict




