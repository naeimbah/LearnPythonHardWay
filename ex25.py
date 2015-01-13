# Breaks sentence into word, splits with ' '
def break_input(inp):
	return inp.split(' ')


# Sorts the words
def sort_input(inp):
	return sorted(inp)


# Print first word after popping it out of the sentence
def print_first(inp):
	out = inp.pop(0)
	print out
	return

# Print last word after popping it out of the sentence
def print_last(inp):
	out = inp.pop(-1)
	print out
	return


# Sorts the sentence
def sort_sentence(sentence):
	words = break_input(sentence)
	return sort_input(words)

# Print first and last word
def print_firstlast(sentence):
	words = break_input(sentence)
	print_first(words)
	print_last(words)

#Print first and last sorted
def print_firstlast_sorted(sentence):
	words = sort_sentence(sentence)
	print_first(words)
	print_last(words)
