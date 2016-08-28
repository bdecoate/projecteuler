def name_score((index, name)):
	"""Calculate the alphabetical score of a name

	:(index, name): a tuple pair containing the index of the name and a double
		quote enclosed name string
	:returns: the name score, for example:
		COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in
		the list. So, COLIN would obtain a score of 938 x 53 = 49714

	"""

	name = name.strip('"')
	names_as_numbers = map(lambda x: ord(x) % ord('A') + 1, name)
	score = sum(names_as_numbers)
	return score * index


with open('p022_names.txt', 'r') as names_file:
	all_names = names_file.readline()

names_alpha_sort = sorted(all_names.split(','))
names_scores = map(name_score, enumerate(names_alpha_sort, 1))
print sum(names_scores)
