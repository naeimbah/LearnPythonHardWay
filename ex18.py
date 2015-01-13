# This one is like the script with argv

def function_two(*args):
	arg1, arg2 = args
	print "\narg1, arg2 are: %r and %r" % (arg1, arg2)

def function_two_v2(arg1, arg2):
	print "\narg1 and arg2: %r and %r" % (arg1, arg2)

def function_one(arg1):
	print "\nargument = %r" % arg1

def function_none():
	print "\nVoid function"


function_two("Sourav", 'Mishra')
function_two_v2("Sourav", "srvmshra")
function_one("sourav")
function_none()
