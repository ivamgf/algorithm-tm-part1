# Algorithm 3 - dataset cleaning and clustering

# Imports
import os
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Downloads
nltk.download('punkt')
nltk.download('stopwords')

# Define the list of stopwords for the Portuguese language
stop_words = set(stopwords.words('portuguese'))

# Create the Stemmer
stemmer = PorterStemmer()

# Use double backslashes in file or directory path
path = "C:\\Dataset"

# Get a list of files in the directory
files = os.listdir(path)

# Print the file list
print("Files found in the directory:")
for file in files:
    print(file)

    # Open the file and read the contents
    with open(os.path.join(path, file), 'r', encoding='utf8') as c:
        content = c.read()

        # Remove the text between the < and > symbols
        content = nltk.re.sub('<.*?>', ' ', content)

        # Tokenize the content in the sentences
        sentences = sent_tokenize(content)

        # Flag for tokenizing and stemming the sentences after the keyword "ACORDAM"
        tokenize_after_keyword = False

        # List to store the filtered sentences
        filtered_sentences = []

        # Filter the sentences without stop words and apply stemming
        for sentence in sentences:
            if "RELATÓRIO" in sentence:
                tokenize_after_keyword = True

            if tokenize_after_keyword:
                # Tokenize each sentence into words
                words = word_tokenize(sentence.lower())

                # Remove stop words
                filtered_words = [
                    word
                    for word in words
                    if word not in stop_words and
                       word not in punctuation
                ]

                # Apply stemming to each word
                words_stemming = [
                    stemmer.stem(word)
                    for word in filtered_words
                ]

                # Put the filtered words together into a sentence again
                filtered_sentence = ' '.join(words_stemming)

                # Add the filtered sentence to the list
                filtered_sentences.append(filtered_sentence)

# Calculate the similarity matrix between sentences
vector = TfidfVectorizer(tokenizer=lambda x: x, lowercase=False)
matrix_similarity = vector.fit_transform(filtered_sentences)

# Execute the results
number_clusters = 4
kmeans = KMeans(n_clusters=number_clusters)
kmeans.fit(matrix_similarity)

# Print the results
print("\nFile: " + file)
print("Sentence clustering:\n")
for i in range(number_clusters):
    print("Cluster ", i+1, ":")
    for j in np.where(kmeans.labels_ == i)[0]:
        print(" - ", sentences[j])
    print("\n")

# Plotting graphs with centroids
centroids = kmeans.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=300, linewidths=3, color='r')
plt.show()
