def add(*arg):
	add1, add2 = arg
	return add1 + add2
def subtract(*arg):
	sub1, sub2 = arg
	return sub1 - sub2
def mult(*arg):
	mult1, mult2 = arg
	return mult1 * mult2
def divn(*arg):
	dividend, divisor = arg
	return dividend/divisor, dividend % divisor

print "Example arithmetic:"

print "5+3 = %d"% add(5,3)
print "5-3 = %d " % subtract(5,3)
print "2*3 = %d " % mult(2,3)
print "(20/3) = %d, %d" % divn(20,3)

final = divn(mult(add(5,3), subtract(5,3)), 10)
print "final = divn(mult(add(5,3), subtract(5,3)), 10) = ", final
