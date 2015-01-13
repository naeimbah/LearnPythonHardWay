# A small python script to truncate files for writing into them
# Needed this when I had to practice programs.

prompt = '> '
print "Truncating file:",
filename = raw_input(prompt)
infile = open(filename, 'w').truncate()
