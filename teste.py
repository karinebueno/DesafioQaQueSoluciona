# Definir o array de palavras
array = ["maça", "banana", "pera"]

# Inicializar uma string vazia para armazenar as primeiras letras
primeiras_letras = ""

# Iterar sobre cada palavra no array
for palavra in array:
    # Adicionar a primeira letra de cada palavra à string
    primeiras_letras += palavra[0]

# Exibir as primeiras letras concatenadas
print(primeiras_letras)  # Saída esperada: "mbp"
