ten_things = "Apples Oranges Crows Cell Light Sugar"
check_list = ten_things.split(' ')
print check_list

more_thing = ["Sun", "Moon", "stars", "galaxy", "earth", "rivers", "lakes"]

while len(check_list)!=10:
	nextitem = more_thing.pop(0)
	print "Adding", nextitem
	check_list.append(nextitem)
	print check_list,">", len(check_list)

print check_list[1]
print check_list[-1]

print check_list.pop()
print ' '.join(check_list)
print '#'.join(check_list[3:6])
