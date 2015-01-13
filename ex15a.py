print "\nFile open:",
print "------------"
prompt = '>'

filename = raw_input(prompt)
txt = open(filename)
print txt.read()
txt.close()
