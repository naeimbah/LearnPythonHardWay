def cheese(count, box):
	print "--" * 20
	print "No of box: %d" % box
	print "Count : %d"    % count
	print "Total ", box + count
	print "--" * 20

def cheese2():
	count = raw_input("count?: ")
	box   = raw_input("boxes?: ")
	print "Total: ", int(count) + int(box)
	print "--" * 20

print 'test zone'
print '-*' * 30
 
cheese(10, 5)
cheese2()

