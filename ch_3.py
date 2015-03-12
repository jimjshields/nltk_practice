import re, nltk

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
ending_in_ed = [w for w in wordlist if re.search('ed$', w)]

class T9(object):
	"""Represents attributes and operations for working w/ T9."""

	def __init__(self, nums):
		self.T_9_LETTERS = {
			1: None,
			2: 'abc',
			3: 'def',
			4: 'ghi',
			5: 'jkl',
			6: 'mno',
			7: 'pqrs',
			8: 'tuv',
			9: 'wxyz'
		}
		self.t_9_numbers = nums
		self.t_9_pattern = ''.join(['[{0}]'.format(self.T_9_LETTERS[num]) for num in self.t_9_numbers])

	def find_t9_words(self):
		self.t_9_words = [w for w in wordlist if re.search('^{0}$'.format(self.t_9_pattern), w)]
		return self.t_9_words

import unittest

class TestT9(unittest.TestCase):
	"""Tests T9 class."""

	def setUp(self):
		self.t9_search = T9([4, 3, 5, 5, 6])

	def test_find_t9_words(self):
		self.assertEqual(self.t9_search.find_t9_words(), [u'hello'])

regexp = r'^[AEIOUaeiou]+|[AEIOU]+$|[^AEIOUaeiou]'

def compress(word):
	pieces = re.findall(regexp, word)
	return ''.join(pieces)

# from nltk.corpus import nps_chat
# from nltk.corpus import gutenberg
# moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# chat = nltk.Text(nps_chat.words())
# print chat.findall(r'<.*><.*><bro>')
# print chat.findall(r'<l.*>{3,}')

raw = """DENNIS: Listen, strange women lying in ponds distributing swords 
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)



# if __name__ == '__main__':
# 	unittest.main()