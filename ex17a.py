# declarations
from sys import argv
from os.path import exists
from random import randint

script, from_file, to_file = argv

# describe operation
print "Copying %s to %s" % (from_file, to_file)
print "%f" % randint(1,100)

# This code works in 2 lines.
#indata = open(from_file).read()
#open(to_file, 'a+').write(indata)


# Attempting to make work in 1 line
open(to_file, 'a+').write(open(from_file).read())


