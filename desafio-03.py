
def beautifulDays(NumeroInicial,NumeroFinal,k):
    contador = 0
    for i in range(NumeroInicial,NumeroFinal+1):
        NumeroInicial_str = str(i)
        NumeroInicial_invertido_str = NumeroInicial_str[::-1]
        NumeroInicial_int = int(NumeroInicial_invertido_str)
        Diferenca = i - NumeroInicial_int
        if Diferenca % k == 0:
            contador = contador + 1
    return(contador)

# NumeroInicial = 20
# NumeroFinal = 23
# k = 6
# resultado = beautifulDays(NumeroInicial,NumeroFinal)
# print(resultado)

print(beautifulDays(20, 23, 6))
print(beautifulDays(13, 45, 3))
print(beautifulDays(1, 2000000, 1000000000))
print(beautifulDays(1, 2000000, 23047885))