from nltk.corpus import gutenberg
import nltk

emma = nltk.Text(gutenberg.words('austen-emma.txt'))

for fileid in gutenberg.fileids():
	num_chars = len(gutenberg.raw(fileid))
	num_words = len(gutenberg.words(fileid))
	num_sents = len(gutenberg.sents(fileid))
	num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))

	print '{0}; Chars: {1}, Words: {2}, Sents: {3}, Vocab: {4}'.format(
		fileid, num_chars, num_words, num_sents, num_vocab)