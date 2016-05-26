import re
from string import ascii_lowercase

alphabet = ascii_lowercase
letter_hit = ''
letter_miss = ''

exclude = letter_miss + letter_miss

print alphabet
print ('exclude' + exclude)

if exclude != '':
	alphabet = re.sub('[%s]' % exclude, '', alphabet)

print alphabet

