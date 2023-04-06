# Algorithm 1 - dataset cleaning

# Imports
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

# Downloads
nltk.download('punkt')
nltk.download('stopwords')

# Define the list of stopwords for the Portuguese language
stop_words = set(stopwords.words('portuguese'))

# Use double backslashes in file or directory path
path = "C:\\Dataset"

# Get a list of files in the directory
files = os.listdir(path)