import os
import nltk
import chardet

# Definir o caminho do diretório
path = "C:\\Dataset"

# Obter uma lista de arquivos no diretório
files = os.listdir(path)

# Definir o texto a ser procurado
text_to_find = "ACORDAM"

# Tokenizar o conteúdo de cada arquivo e imprimir somente as sentenças que contêm o texto desejado
for file in files:
    if file.endswith('.rtf'):  # Somente processa arquivos rdf
        with open(os.path.join(path, file), 'rb') as f:
            resultado = chardet.detect(f.read())
            codificacao = resultado['encoding']

        with open(os.path.join(path, file), 'r', encoding=codificacao) as f:
            content = f.read()
            sentences = nltk.sent_tokenize(content)
            print("Sentenças encontradas no arquivo " + file + " que contêm o texto '" + text_to_find + "':")
            for sentence in sentences:
                if text_to_find in sentence and '<' not in sentence and '>' not in sentence:
                    print(sentence)
