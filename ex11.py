# Prompting input by use raw_input()

print "How old are you?",
age = raw_input()

print "How tall?",
height = raw_input()

print "how heavy",
weight = raw_input()

print "This is my vitals %r %r %r" % (age,height,weight)

print "Doing some advanced type-cast"

weight = float(weight)
height = int(height)
age = int(age)

print "This is my vitals %d %d %f" % (age,height,weight)


