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

my_sol = '    a'
tried = ''

print solRegex(my_sol,tried)
