import os
import nltk

# Definir o caminho do diretório
path = "C:\\Dataset"

# Obter uma lista de arquivos no diretório
files = os.listdir(path)

# Definir o texto a ser procurado
text_to_find = "RELATORIO"

# Tokenizar o conteúdo de cada arquivo e imprimir as sentenças anterior à sentença que contêm o texto desejado
for file in files:
    if file.endswith('.rtf'):  # Somente processa arquivos RTF
        with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = nltk.sent_tokenize(content)
            print("Sentenças encontradas no arquivo " + file + " que contêm o texto '" + text_to_find + "':")
            for sentence in sentences:
                if text_to_find in sentence:
                    print(sentence)
                    break
                else:
                    print(sentence)

