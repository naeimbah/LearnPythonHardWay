# An assignment operation and also a string

print "some assignment for x and y you can't see now."

# The string evaluates the value of %d and then the whole string assigned to x
x = "There are %d types of people" % 2

#Assigning 2 string constants - single and double quotes
binary = 'binary'
do_not = "don't"

#string constants in a string formatted output and then assigning

y = "Those who know %s and those who %s" % (binary,do_not)


print "Now printing x and y:"
print x
print y

print "See the use of r escape character:"
print "I said for x: %r" % x
print "I said for y: %s" % y


# Using string assigned to a variable and printing.
# joke_eval is a string with a format output placeholder. Hilarious is boolean

joke_eval = "Is the joke funny? %r"
no = False
print joke_eval % no

# Combining another 2 strings assigned as variables.
w = "This is left side of"
e = " a string with a right side"
print w+e

print "Difference in %r and %s outputs."
print "Test %r" % (w+e)
print "Test %s" % (w+e)
