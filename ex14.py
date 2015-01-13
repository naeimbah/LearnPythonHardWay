from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I am %s" % (user_name,script)
print "Do you like me?"
response1 = raw_input(prompt)

print "Tell me your address"
response2 = raw_input(prompt)

print "So we know these: \nYour response %s \nYour address %s" % (response1,response2)
