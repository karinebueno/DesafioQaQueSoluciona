import math

def encryption (s):
    s_sem_espaco = s.replace(" " , "")
    NumeroDeElementos = len(s_sem_espaco)
    raiz_de_s = math.sqrt(NumeroDeElementos)
    NumeroDeLinhas = math.floor(raiz_de_s)
    NumeroDeColunas = math.ceil(raiz_de_s)

    resultado = []
    for i in range(0,NumeroDeElementos,NumeroDeColunas):
        resultado.append(s_sem_espaco[i:i + NumeroDeColunas]) #string[start:end]

    matriz = []

    for i in range(NumeroDeLinhas):
        linha = []
        for j in range(NumeroDeColunas):
            index = i * NumeroDeColunas + j
            if index < NumeroDeElementos:
                linha.append(s_sem_espaco[index])
            else:
                linha.append('')  # Preencher com string vazia se estiver fora do limite
        matriz.append(linha)

    palavras = []
    for col in range(NumeroDeColunas):
        palavra = ""
        for linha in matriz:
            if linha[col] != '':  # Ignorar preenchimento vazio
                palavra += linha[col]
        palavras.append(palavra)

    return palavras

s = "have a nice day"

resultadofinal = encryption(s)

print(resultadofinal)














# Matriz=[]
# for i in range(len(Array)):
#
#     Matriz = Array[i]
#     #Matriz = ArrayLinha1
#
#
#     print(Matriz)
#     #print(ArrayLinha1)





# resultados = []
# for i in range(4):
#     resultado = []
#     for i in range(0,NumeroDeElementos,NumeroDeColunas):
#         resultado.append(s_sem_espaco[i:i + NumeroDeColunas]) #string[start:end]
#     resultados.append(resultado)

# resultadofinal = ""
# for resultado in resultados:
#     for palavra in resultado:
#         if palavra:  # Verifica se a palavra não está vazia
#             resultadofinal = resultadofinal + palavra[0]