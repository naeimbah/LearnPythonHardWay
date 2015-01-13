count = [1, 2, 3, 4, 5]
item = ['apple', 'orange', 'grape', 'pineapple']
change = [1, 'pennies', 2, 'dime', 3, 'quarter']

for number in count:
	print "\nMy count %d" % number

for fruit in item:
	print "\nThe item is %s" % fruit

for i in change:
	print "change value = %r" % i

# Building lists:
elements = []

# range automatically spawns out number from 0->6
for n in range(0,6):
	print "Adding %d \n" % n
	elements.append(n)

for n in elements:
	print "\n> %d" % n
