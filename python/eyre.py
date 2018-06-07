import nltk
# Imports a package called "nltk" and loads it for this file.

our_file = "eyre.txt"
# Set a variable filename for where our file is.

def open_file_and_get_text(filename):
    with open(filename, "r") as our_file:
    # Given a filename, open it ("r" means read-only file).
        text = our_file.read()
        # Takes the file and reads the text. Stores itself.
    return text

def clean_tokens(words):
# Given some tokens, lowercase them all.
    clean_words = []
    # Creates an empty list called "clean_words."
    for word in words:
    # Loop over every word item in the words list.
        clean_words.append(word.lower())
        # Make each word lowercase and append it to the new list.
    return clean_words

text = open_file_and_get_text(our_file)

words = nltk.word_tokenize(text)
# Takes a long string and breaks it into words.
clean_words = clean_tokens(words)
print(clean_words[0:30])
# Print out first 29 words of our clean tokens.

word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts["jane"])
nltk.Text(clean_words).dispersion_plot(["he", "she", "jane", "tony"])
