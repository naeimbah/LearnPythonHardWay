
# define the class

class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me(self):
		for line in self.lyrics:
			print line

happybday = Song(["Happy Birthday to you",
		  "I dont want to get sued",
		  "I'll stop right here"])

happybday.sing_me()
