from bs4 import BeautifulSoup
from urllib import request
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

def normalize(tokens):
    normalized = [token.lower() for token in tokens]
    end_of_front_matter = 90
    start_of_end_matter = -2973
    normalized = normalized[end_of_front_matter:start_of_end_matter]
    return normalized

def remove_stopwords(tokens):
    return [token for token in tokens if token not in stopwords.words('english')]

def get_counts_in_corpora(token, corpus_one, corpus_two):
    corpus_one_counts = [text_freq_dist[token] for text_freq_dist in corpus_one]
    corpus_two_counts = [text_freq_dist[token] for text_freq_dist in corpus_two]
    return  [corpus_one_counts, corpus_two_counts]

url = "https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/full-text.txt"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
texts = eval(soup.text)

tokenized_texts = []
for text in texts:
    tokenized_texts.append(word_tokenize(text))

doyle = tokenized_texts[:5]
bronte = tokenized_texts[5:]
doyle = [normalize(text) for text in doyle]
bronte = [normalize(text) for text in bronte]

print(len(doyle[0]))
print('start cleaning')
doyle = [remove_stopwords(text) for text in doyle]
print('doyle done')
bronte = [remove_stopwords(text) for text in bronte]
print('bronte done')
