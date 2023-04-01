import os
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Use barras invertidas duplas no caminho do arquivo ou diretório
path = "C:\\Users\\Lamid\\Documents\\Dataset"

# Obter uma lista de arquivos no diretório
files = os.listdir(path)

# Imprimir a lista de arquivos
print("Arquivos encontrados no diretório:")
for file in files:
    print(file)

    # Abrir o arquivo e ler o conteúdo
    with open(os.path.join(path, file), 'r', encoding='utf8') as f:
        content = f.read()

        # Tokenizar o conteúdo em sentenças
        sentences = sent_tokenize(content)

        # Imprimir as sentenças
        print("Sentenças no arquivo " + file + ":")
        for sentence in sentences:
                print(sentence)
