import math

def NumerosInteirosQudrados(entrada,saida):
    raiz_entrada = math.ceil(math.sqrt(entrada))
    raiz_saida = math.floor(math.sqrt(saida))

    if raiz_saida >= raiz_entrada:
        return raiz_saida - raiz_entrada + 1
    else:
        return 0

entrada = 12
saida = 999999988

resultado = NumerosInteirosQudrados(entrada, saida)

print(resultado)




# import math

#Entrada = 59
#Saida = 999999966
#contador = 0

#for ...range(start,stop)
#for Entrada in range (Entrada, Saida +1):
#  raiz_quadrada = Entrada ** 0.5
#  valorInteiro = int(raiz_quadrada)
#  if valorInteiro * valorInteiro == Entrada:
#      contador = contador + 1
#print(contador)

# Entrada = 24
# Saida = 49
# contador = 0
#
#
# for Entrada in range (Entrada, Saida +1):
#     raiz_quadrada = math.sqrt(Entrada)
#     if raiz_quadrada == int(raiz_quadrada):
#         contador = contador + 1
# print(contador)


# import math
#
# Entrada = 12
# primeiro = 1
# Saida = 999999988
#
# def NumerosInteirosQuadrados(primeiro,Saida):
#     inteiros_quadrados = []
#     for num in range(primeiro,Saida+1):
#         raiz_quadrada_num = math.sqrt(num)
#         arredonda_baixo = math.floor(raiz_quadrada_num)
#         numero_ao_quadrado = arredonda_baixo * arredonda_baixo
#         if numero_ao_quadrado == num:
#             inteiros_quadrados.append(num)
#     return(inteiros_quadrados)
#
# inteiros_quadrados = NumerosInteirosQuadrados(primeiro,Saida)
# print(inteiros_quadrados)
#
# raiz_quadrada_Entrada = math.ceil(math.sqrt(Entrada))
# valorInicial = raiz_quadrada_Entrada * raiz_quadrada_Entrada
# contador = 0
# for num in inteiros_quadrados:
#     if num >= valorInicial:
#         contador = contador + 1
# print(contador)






# for i in range(raiz_quadrada_Entrada, NumerosInteirosQuadrados(num) +1):
#     contador = contador + 1
# print(contador)









