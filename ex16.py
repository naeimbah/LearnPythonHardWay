from sys import argv
script, filename = argv

print "Name of text file to erase : %s" % filename
print "To continue, press RETURN",
raw_input("?")

target = open(filename, 'w')
print "Truncating ..."
target.truncate()

print "Get new lines > "
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Writing the three lines"

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
target.write('\0')

target.close()
