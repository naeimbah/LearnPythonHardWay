# creating a map

states = {
	'Oregon'  : 'OR',
	'Florida' : 'FL',
	'New York' : 'NY',
	'Michigan' : 'MI'}

cities = {'CA' : 'San Francisco',
	  'MI' : 'Detroit',
	  'FL' : 'Jacksonville',
	  'MA' : 'Boston'}

# add some more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'
states['Massachussets'] = "MA"

# print

print '- ' * 40
print "New York : ", cities['NY']
print "Oregon	: ", cities['OR']
print "Michigan abbrev:", states['Michigan']
print "Florida abbrev :", states['Florida']

print '- ' * 40
print "Michigan has", cities[states['Michigan']]
print "New York has", cities[states['New York']]

# Special use. See how the formatting is done.

print "* " * 40
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state,abbrev)

print "* " * 40
for abbrev,city in cities.items():
	print "%s is abbreviated %s" % (abbrev,city)

print "* " * 40
for state, abbrev in states.items():
	print "%s \t%s \t%s" % (state, abbrev, cities[abbrev])

print '* ' * 40
state = states.get('Texas', None)
if not state:
	print "Sorry"

city = cities.get('TX', 'Does not exist')
print "City for state 'TX' %s" % city

