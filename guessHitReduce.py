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


				