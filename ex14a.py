from sys import argv

script, user_name = argv
prompt = '$'

print "Hi %s, I am %s" % (user_name,script)
print "Do you like me?"
response1 = raw_input(prompt)

print "Tell me your address"
response2 = raw_input(prompt)
print "Tell me your city"
response3 = raw_input(prompt)

print '''We know these
as the responses the user %s made: %s %s''' % (user_name, response2, response3)

