# Review exercise

print "\nYou\'d need to know about \"escape\" characters\b"
print '''\nMary had a little lamb,
	it\'s fleece was white as snow,
	And everywhere that Mary went,
	the lamb was sure to go'''

print '-' * 40
x = 'Value of variable is %d' % 20
print x
print '-' * 40

myVar = 18/(2*3)
myRem = 18 % (2*3)
print "\nMy variable is",myVar,myRem,"!"


def powterm(*argv):
	num, ind = argv
	return num^ind, num*ind 

term1, term2 = powterm(4,3)
print "4^3 and 4*3", term1, term2
