class Other(object):
	def implicit(self):
		print "other self"
	def override(self):
		print "other override"
	def alter(self):
		print "other alter"

class Child(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()
	def override(self):
		print "child Override"	
	def alter(self):
		self.other.alter()

prog = Child()
prog.implicit()
prog.override()
prog.alter()
