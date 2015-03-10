from nltk.corpus import gutenberg, webtext, brown, reuters, inaugural, udhr
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

# Conditional Freq Dist - takes a list of pairs/tuples
def get_cfd_count_by_genre():
	cfd = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories=genre))
	return cfd

def get_words_for_genres(genres):
	genre_word = [(genre, word)
		for genre in genres
		for word in brown.words(categories=genre)]
	return genre_word

def get_cfd(conditional_word_list):
	"""Returns a cfd for a given conditional word list."""

	return nltk.ConditionalFreqDist(conditional_word_list)

# print get_cfd(get_words_for_genres(['news', 'romance']))['news']['will']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
words = ['news']
# for i in get_f_dist_for_word_list('news', words):
# 	print i

def get_conditional_freq_dist(categories, word_list):
	cfd = nltk.ConditionalFreqDist((genre, word) 
		for genre in brown.categories()
		for word in brown.words(categories=genre))
	return cfd.tabulate(conditions=categories, samples=word_list)

# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# print get_conditional_freq_dist(genres, modals)

def get_inaugural_plot():
	cfd = nltk.ConditionalFreqDist((target, fileid[:4])
		for fileid in inaugural.fileids()
		for w in inaugural.words(fileid)
		for target in ['america', 'citizen']
		if w.lower().startswith(target))
	return cfd.plot()

def get_cfd_for_udhr():
	languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
	cfd = nltk.ConditionalFreqDist(
		(lang, len(word))
		for lang in languages
		for word in udhr.words(lang + '-Latin1'))
	return cfd.plot(cumulative=True)

sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
def generate_model(cfdist, word, num=15):
	for i in range(num):
		print word,
		word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

def unusual_words(text):
	"""Returns a sorted list of unusual words as compared to the Unix words list."""

	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)

def content_fraction(text, non_content):
	"""Returns a float representing percentage of a text not in the non_content list."""

	content = [w for w in text if w.lower() not in non_content]
	return float(len(content)) / float(len(text))


# from nltk.corpus import stopwords
# stopwords = stopwords.words('english')

def solve_word_puzzle(puzzle_letters, obligatory_letter, length=9):
	wordlist = nltk.corpus.words.words()
	return [w for w in wordlist if len(w) >= length and nltk.FreqDist(w) <= nltk.FreqDist(puzzle_letters)]

def male_and_female_names():
	names = nltk.corpus.names
	male_names = names.words('male.txt')
	female_names = names.words('female.txt')
	return [w for w in male_names if w in female_names]

def cfd_plot_by_name_letter(letter_index):
	names = nltk.corpus.names
	cfd = nltk.ConditionalFreqDist((fileid, name[letter_index])
			for fileid in names.fileids()
			for name in names.words(fileid))
	return cfd.plot()

def pronouncing_dict():
	entries = nltk.corpus.cmudict.entries()
	for entry in entries[39943:39951]:
		print entry

pronouncing_dict()