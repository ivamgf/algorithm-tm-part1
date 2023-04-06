import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

nltk.download('punkt')
nltk.download('stopwords')

# Define a lista de stopwords para a língua portuguesa
stop_words = set(stopwords.words('portuguese'))

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

        # Remover o texto entre os símbolos < e >
        content = nltk.re.sub('<.*?>', '', content)

        # Tokenizar o conteúdo em sentenças
        sentences = sent_tokenize(content)

        # Imprimir as sentenças sem as stop words
        print("Sentenças no arquivo " + file + " sem as stop words:")
        for sentence in sentences:
            # Tokenizar cada sentença em palavras
            words = word_tokenize(sentence.lower())

            # Remover as stop words
            filtered_words = [word for word in words if word not in stop_words and word not in punctuation]

            # Reunir as palavras filtradas em uma sentença novamente
            filtered_sentence = ' '.join(filtered_words)

            # Imprimir a sentença filtrada
            print(filtered_sentence)
