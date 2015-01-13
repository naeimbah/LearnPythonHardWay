# Optimization comment - checking upto sqrt(num) ->  O(sqrt(N))
# better techniqe than A) making prime number list B) O(N) techniques

from sys import argv
from math import sqrt
script, number = argv
number = int(number)

if number < 0:
	number = (-number)
	print "Inverting sign & checking modulus"
	print "(Natural numbers)"
elif number == 1:
	print "Neither prime or composite"
elif number == 0:
	print "Not defined for natural number systems"


for n in range(2, int(sqrt(number)+1)):
	if (number % n) == 0:
		print "number is composite"
		exit(0)
	
print "Number is prime"

