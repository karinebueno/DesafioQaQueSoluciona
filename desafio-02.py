def countingValleys(caminhadas):
    nivel = 0
    vales = 0
    AbaixoNivelDoMar = False

    for passo in caminhadas:
        if passo == 'U':
            nivel = nivel + 1
        elif passo == 'D':
            nivel = nivel - 1

        if nivel < 0 and not AbaixoNivelDoMar:
            AbaixoNivelDoMar = True

        if nivel == 0 and AbaixoNivelDoMar:
            vales = vales + 1
            AbaixoNivelDoMar = False

    return(vales)


caminhadas = "UDDDUDUU"

resultadofinal = countingValleys(caminhadas)

print(resultadofinal)