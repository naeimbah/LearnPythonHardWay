# test program 

def printhisto(*args):
	name, number = args
	print "%s" % name,"* " * number
	return

while True:
	print "\nEnter input:"
	argv = raw_input(">")
	items = argv.split(" ")
	print items	
	if len(items)%2 != 0:
		items.pop(-1)
	print "Number of items: ", len(items)/2
	nam = [] 		#initialize the lists
	num = []

	for i in range(0, (len(items)/2)):
		nam.append(str(items[2*i]))
		num.append(int(items[2*i + 1]))
		printhisto(nam[i], num[i])
