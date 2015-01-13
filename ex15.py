from sys import argv
script,filename = argv

txt = open(filename)
print "\nHere's the file name : %s" % filename
print txt.read()

print "\nGet a new filename:"
filename2 = raw_input("> ")
txt2 = open(filename2)
print txt2.read()


