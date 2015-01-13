from sys import argv
script, input_file = argv

# Prints everything in file
def print_all(f):
	print f.read()
# Go back to where the file started
def rewind(f):
	f.seek(0)
# Print a designated number of lines.
def print_line(f, linecount):
	print linecount,">", f.readline()


# create a file object
current_file = open(input_file)
print "print everything"
print_all(current_file)

print "Go back to the beginning"
rewind(current_file)

print "Print a specific line"
countline = 1
print_line(current_file,countline)

countline += 1
print_line(current_file,countline)

countline += 1
print_line(current_file,countline)
