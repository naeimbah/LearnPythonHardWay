from sys import argv
script, A, B = argv

A = int(A)
B = int(B)

if A > B:
	print "A > B"
elif A < B:
	print "A < B"
else:
	print "A = B"
