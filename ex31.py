print "Choose first stage input\n"
firstin = raw_input(">")

if firstin == "1":
	print "Stage 2: choose 1-1 or 1-2"
	secondin = raw_input('>')
	if secondin == "1-1":
		print "This is 1 -> 1"
	elif secondin == "1-2":
		print "This is 1 -> 2"
	else:
		print "Invalid input"

elif firstin == "2":
	print "Stage 2: choose 2-1 or 2-2"
	secondin = raw_input(">")
	if secondin == "2-1":
		print "2 -> 1"
	elif secondin == "2-2":
		print "2 -> 2"
	else:
		print "Invalid"
else:
	print "Not valid execution"


