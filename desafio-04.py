import math

def activityNotificatins(n,d):

    contador = 0
    for i in range(d, len(n)):
        soma = sum(n[i-d:i])
        mediana = soma / d
        mediana_arredondado = math.ceil(mediana)
        despesaDoDia= n[i]
        if despesaDoDia >= 2*mediana:
            contador = contador + 1
    return contador

#n = [2,3,4,2,3,6,8,4,5]
#n = [1, 2, 3, 4, 4]
#n = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n = [1, 2, 100, 2, 2, 2, 2, 2]
d = 4

resultado = activityNotificatins(n,d)

print(resultado)

#for i in range(len(n)):
#    print(i, n[i])