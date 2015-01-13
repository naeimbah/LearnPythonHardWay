from sys import exit

def gold_room():
	print "Gold room. Requirement?"	
	next = raw_input(">")

	if "0" in next or "1" in next:
		quant = int(next)
	else:
		dead("type something")
	
	if quant < 50:
		print "not greedy"
		exit(0)

	else:
		dead("greedy!")

# gold_room has a strange way of if condition check. " "0" in next or "1" in next. This can be avoided by writing, next < 2. Also what if a larger number is given.


def bear_room():
	print "How much will you move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
	
		if next == "take":
			dead("bear slaps you")
		elif next == "taunt" and not bear_moved:
			dead("Go through door quick")
		elif next == "taunt" and bear_moved:
			dead("Bear is angry")
		elif next == "open" and bear_moved:
			gold_room()
		else:
			print "No idea"

# while True: is making a infinite loop. Similar to while(1) in C. The exit is from one of the conditions inside, which will terminate with a exit(0) or jump tp gold room



def devil_room():
	print "Room of devil"
	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		print "that was tasty"
	else:
		devil_room()

def dead(why):
	print why, "good job"
	exit(0)

def start():
	print "You are in dark room"
	print "A door to left and right"
	
	next = raw_input("> ")
	if next == "left":
		bear_room()
	elif next == "right":
		devil_room()
	else:
		dead("Stumble around and starve")

start()
