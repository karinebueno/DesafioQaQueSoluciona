
def similarity(s):

    tamanhoDaString = len(s)
    resultado = tamanhoDaString


    for i in range(1,tamanhoDaString):
        sufixo = s[i:] #string[start:end] #vai me retornar o sufixo apartir do indice i
        for j in range(len(sufixo)):
            if sufixo[j] == s[j]:
                resultado = resultado + 1
            else:
                break
    return(resultado)

s = "ababaa"

resultadofinal = similarity(s)

print(resultadofinal)