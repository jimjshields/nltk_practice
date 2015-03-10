from nltk.corpus import gutenberg, webtext, brown
import nltk

def get_text(fileid):
	text = nltk.Text(gutenberg.words(fileid))
	return text

def get_stats():
	for fileid in gutenberg.fileids():
		num_chars = len(gutenberg.raw(fileid))
		num_words = len(gutenberg.words(fileid))
		num_sents = len(gutenberg.sents(fileid))
		num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))

		print '{0}; Chars: {1}, Words: {2}, Sents: {3}, Vocab: {4}'.format(
			fileid, num_chars, num_words, num_sents, num_vocab)

def get_sentences(fileid):
	text_sents = gutenberg.sents(fileid)
	return text_sents

def get_webtext():
	for fileid in webtext.fileids():
		print fileid, webtext.raw(fileid)[:10]

def get_brown_categories():
	return brown.categories()

def get_brown_words(categories):
	return brown.words(categories=categories)

def get_f_dist_for_word_list(categories, word_list):
	f_dist = nltk.FreqDist(w.lower() for w in get_brown_words(categories))
	return ((word, f_dist[word]) for word in word_list)

modals = ['can', 'could', 'may', 'might', 'must', 'will']
words = ['news']
# for i in get_f_dist_for_word_list('news', words):
# 	print i

def get_conditional_freq_dist(categories, word_list):
	cfd = nltk.ConditionalFreqDist((genre, word) 
		for genre in brown.categories()
		for word in brown.words(categories=genre))
	return cfd.tabulate(conditions=categories, samples=word_list)

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
print get_conditional_freq_dist(genres, modals)