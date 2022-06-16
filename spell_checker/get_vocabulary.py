import re
import pickle
import zipfile
from collections import Counter


def unzip_vocabulary():
    with zipfile.ZipFile("assets/vocabulary.zip", "r") as zip_ref:
        zip_ref.extractall("assets")

try:
    file=open('assets/vocabulary.txt',encoding='utf-8').read()
except FileNotFoundError:
    unzip_vocabulary()
    file=open('assets/vocabulary.txt',encoding='utf-8').read()

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def words(text):
  return re.findall(r'\w+', text.lower())

file=remove_tags(file)
WORDS = Counter(words(file))

WORDS=Counter({word:count for word, count in WORDS.items() if count >1 })



with open('/assets/vocabulary.pickle', 'wb') as outputfile:
    print(outputfile) 
    print(pickle.dump(WORDS, outputfile))

del WORDS
