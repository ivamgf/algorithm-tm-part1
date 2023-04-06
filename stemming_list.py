import os
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

# Define a lista de stopwords para a lingua portuguesa
stop_words = set(stopwords.words('portuguese'))

# Cria o stemmer
stemmer = PorterStemmer()

# Use barras invertidas duplas no caminho do arquivo ou diretório
path = "C:\\Dataset"

# Obter uma lista de arquivos no diretório
files = os.listdir(path)

# Imprimir a lista de arquivos
print("Arquivos encontrados no diretório:")
for file in files:
    print(file)

    # Abrir o arquivo e ler o conteúdo
    with open(os.path.join(path, file), 'r', encoding='utf8') as f:
        content = f.read()

        # Remove o texto entre < e >
        content = re.sub('<.*?>', '', content)

        # Remove pontuação e caracteres especiais
        content = re.sub('[^\w\s]', '', content)

        # Tokeniza o conteúdo em palavras
        words = word_tokenize(content.lower())

        # Remove as stopwords
        words = [word for word in words if word not in stop_words]

        # Aplica o stemming em cada palavra
        words = [stemmer.stem(word) for word in words]

        # Imprime as palavras
        print("Palavras no arquivo " + file + ":")
        print(words)
