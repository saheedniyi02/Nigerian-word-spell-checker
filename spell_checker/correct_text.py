import re
import pickle
import zipfile
from collections import Counter



def edit_once(word):
    "All edits that are one edit away from `word`."
    letters    = 'aáàbcdeéèfghiíìjklmnoóòpqrstuúùvwxyz'
    split_words     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in split_words if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in split_words if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in split_words if R for c in letters]
    inserts    = [L + c + R               for L, R in split_words for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edit_twice(word):
  return (edit2 for edit1 in edit_once(word) for edit2 in edit_once(edit1))



with open('/assets/vocabulary.pickle', 'rb') as inputfile:
    WORDS=pickle.load(inputfile)


#returns the count of a word
def P(word, N=sum(WORDS.values())):
  return WORDS[word] / N

#returns only words in our vocabulaty
def known(words):
  return set(w for w in words if w in WORDS)

def candidates(word):
  return known([word])or known(edit_once(word)) or known(edit_twice(word)) or [word]

def correction(word):
  return max(candidates(word), key=P)


def case_of(text):
    "Return the case-function appropriate for text: upper, lower, title, or just str."
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.title if text.istitle() else
            str)
    
    
def correct_match(match):
    "Spell-correct word in match, and preserve proper upper/lower/title case."
    word = match.group()
    return case_of(word)(correction(word.lower()))

def correct_text(text):
    "Correct all the words within a text, returning the corrected text."
    return re.sub('[a-zA-Z]+', correct_match, text)


