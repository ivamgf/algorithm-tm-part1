import os

# Use barras invertidas duplas no caminho do arquivo ou diretório
path = "C:\\Users\\Lamid\\Documents\\Dataset"

# Obter uma lista de arquivos no diretório
files = os.listdir(path)

# Imprimir a lista de arquivos
print("Arquivos encontrados no diretório:")
for file in files:
    print(file)

