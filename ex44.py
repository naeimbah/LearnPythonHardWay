class Parent(object):
	def override(self):
		print "Parent override"
	def implicit(self):
		print "Parent implicit"
	def alter(self):
		print "parent altered"

class Child(Parent):
	def override(self):
		print "Child override"
	def alter(self):
		print "\n\tbefore"
		super(Child,self).alter()
		print "\tafter"

father = Parent()
child  = Child()
 
father.implicit()
child.implicit()

father.override()
child.override()

father.alter()
child.alter()
