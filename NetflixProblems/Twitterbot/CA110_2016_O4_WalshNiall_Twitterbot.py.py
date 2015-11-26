import random
import twitterbot
corpuspath = raw_input("Enter the full filepath of your corpus: ")
tweetsize = raw_input("Enter the size you wish your tweets to be: ")
corpus = open (corpuspath)
class Twitterbot(object):
	def __init__(self, open_file):
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()
	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words
	def triples(self):
		if len(self.words) < 3:
			return
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
	def database(self):
		for word1, word2, word3 in self.triples():
			key = (word1, word2)
			if key in self.cache:
				self.cache[key].append(word3)
			else:
				self.cache[key] = [word3]
	def generate_tweet(self, size= int(tweetsize)):
		seed = random.randint(0, self.word_size-2)
		seedword = self.words[seed]
		nextword = self.words[seed+1]
		word1, word2 = seedword, nextword
		generatewords = []
		for i in xrange(int(tweetsize)):
			generatewords.append(word1)
			word1, word2 = word2, random.choice(self.cache[(word1, word2)])
		generatewords.append(word2)
		tweetunformat = ' '.join(generatewords)+'.'
		tweetformat = tweetunformat[0].upper() + tweetunformat[1:]
		print tweetformat
choice = raw_input()
while choice == "":
 for i in range(100):
    tweet = twitterbot.Twitterbot(corpus)
    tweet.generate_tweet()
    choice = raw_input()


