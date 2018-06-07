from bs4 import BeautifulSoup
from urllib import request

import nltk
from nltk import word_tokenize

from nltk.corpus import stopwords
#print(stopwords.words('english')[0:30])

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

def normalize(tokens):
    normalized = [token.lower() for token in tokens]
    end_of_front_matter = 90
    start_of_end_matter = -2973
    normalized = normalized[end_of_front_matter:start_of_end_matter]
    return normalized

doyle = [normalize(text) for text in doyle]
bronte = [normalize(text) for text in bronte]

#print(doyle[0][:30])

def remove_stopwords(tokens):
    return [token for token in tokens if token not in stopwords.words('english')]

#print(len(doyle[0]))
#print('start cleaning')
#doyle = [remove_stopwords(text) for text in doyle]
#print('doyle done')
#bronte = [remove_stopwords(text) for text in bronte]
#print('bronte done')

#print(len(doyle[0]))

#example = nltk.FreqDist(doyle[0])
#print(example.most_common(20))

doyle_freq_dist = [nltk.FreqDist(text) for text in doyle]
bronte_freq_dist = [nltk.FreqDist(text) for text in bronte]

def print_top_words(freq_dist_text):
    """Takes a frequency distribution of a text and prints out the top 10 words in it."""
    #print('=====')
    return(freq_dist_text.most_common(10))
    #print('=====')

for text in doyle_freq_dist:
    print_top_words(text)
for text in bronte_freq_dist:
    print_top_words(text)

#print(doyle_freq_dist[0]['holmes'])
#print(bronte_freq_dist[0]['would'])

def get_counts_in_corpora(token, corpus_one, corpus_two):
    corpus_one_counts = [text_freq_dist[token] for text_freq_dist in corpus_one]
    corpus_two_counts = [text_freq_dist[token] for text_freq_dist in corpus_two]
    return  [corpus_one_counts, corpus_two_counts]

#print(get_counts_in_corpora('evidence', doyle_freq_dist, bronte_freq_dist))
#print(get_counts_in_corpora('reader', doyle_freq_dist, bronte_freq_dist))
#print(get_counts_in_corpora('!', doyle_freq_dist, bronte_freq_dist))
#print(get_counts_in_corpora('?', doyle_freq_dist, bronte_freq_dist))

results = get_counts_in_corpora('!', doyle_freq_dist, bronte_freq_dist)
corpus_one_results = results[0]
corpus_two_results = results[1]

#print(corpus_one_results)
#print(corpus_two_results)

nltk.Text(doyle[0]).dispersion_plot(['evidence', 'clue', 'science', 'love', 'say', 'said'])
nltk.Text(bronte[0]).dispersion_plot(['evidence', 'clue', 'science', 'love', 'say', 'said'])
