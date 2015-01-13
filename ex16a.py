from sys import argv
script, filename = argv

print "Name of text file to erase : %s" % filename
print "Should you continue (press RETURN)",
raw_input("?")

target = open(filename, 'w')
print "\nTruncating ..."
target.truncate()

print "Get new lines > "
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Writing the three lines"
combineLine = line1 + '\n' + line2 + '\n' + line3
print "Combined line : %s" % combineLine
target.write(combineLine)
target.write('\0')

target.close()
