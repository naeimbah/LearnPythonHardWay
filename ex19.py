def cheese(count, box):
	print "--" * 20
	print "No of box: %d" % box
	print "Count : %d"    % count
	print "--" * 20

print 'test zone'
cheese(10, 5)

print "only variables"
new_count = 20
new_box   = 10
cheese(new_count, new_box)

print "only math"
cheese(10*20, 30*10)


print "variable and math"
cheese(new_count + 10*20, new_box + 10*30)
