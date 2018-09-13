# Download wiki corpus from https://dumps.wikimedia.org/hewiki/latest/
from gensim.corpora import WikiCorpus

inp = "hewiki-latest-pages-articles.xml.bz2"
outp = "wiki.he.text"
i = 0

print("Starting to create wiki corpus")
output = open(outp, 'w')
space = " "
wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
print("Finished reading WikiCorpus")
for text in wiki.get_texts():
	try:
		article = space.join([t for t in text])
		output.write("{}\n".format(article))
		i += 1
		if (i % 100 == 0):
			print("Saved " + str(i) + " articles")
	except:
		try:
			print("Error, skipping the article: "+article)
		except:
			print("Double Error! No article to print")
output.close()
print("Finished - Saved " + str(i) + " articles")
