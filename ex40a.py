# Additonal exercise
# define the class

class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me(self):
		for line in self.lyrics:
			print line
	def words(self):
		for line in self.lyrics:
			print line.split(' ')
		return


song = ['The saints are coming', 'Tu jaane na', 'jab we met']

happybday = Song(song)
happybday.sing_me()
happybday.words()
