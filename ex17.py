from sys import argv
from os.path import exists

# define the parts from CLI argument
script, from_file, to_file = argv

# describe operation
print "Copying %s to %s" % (from_file, to_file)

infile = open(from_file)
indata = infile.read()

print "Length of file in bytes", len(indata)
print "Does output file exist? %r" % exists(to_file)
print "Hit Return to continue"
raw_input()

outfile = open(to_file, 'a+')
outfile.write(indata)
outfile.close()
infile.close()
