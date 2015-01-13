from sys import argv
script, first, second, third = argv

print "Script name : ", script
print "first value : ", first
print "second value: ", second
print "third value : ", third

while True:
	y = raw_input(">> ")
	print "Another input:  %r " % y
