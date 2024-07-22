def ReconstruindoFrase(login_attempt, passwords):
    result = []
    while login_attempt:
        for password in passwords:
            if login_attempt.startswith(password):
                result.append(password)
                login_attempt = login_attempt[len(password):]
                found = True
                break
        if not found:
            return None
    return result

#Lista de senhas
passwords = ["because", "can", "do", "must", "we", "what"]
# Tentativa de login
login_attempt = "wedowhatwemustbecausewecan"

# Reconstruir a frase
SaidaEsperada = ReconstruindoFrase(login_attempt, passwords)

if SaidaEsperada:
    # Juntar as palavras com espaço
    SenhaFinal = " ".join(SaidaEsperada)
    print(SenhaFinal)
else:
    print("WRONG PASSWORD")


# passwords = ["because", "can", "do", "must", "we", "what"]
# loginAttempt = []
#
# def passwordCracker(passwords,loginAttempt):
#     passwords = ["because", "can", "do", "must", "we", "what"]
#     loginAttempt = (passwords[4] + " " + passwords[2] + " " + passwords[5] + " " + passwords[4] + " " + passwords[3]
#                     + " " + passwords[0] + " " + passwords[4] + " " + passwords[1])
#     return(loginAttempt)
#
#
# Saida = passwordCracker(passwords,loginAttempt)
# print(Saida)


import itertools

# array = ["a", "b", "c"]

# Gerar todas as combinações possíveis (excluindo o conjunto vazio)
# combinacoes = []
# for r in range(1, len(array) + 1):
#     combinacoes.extend(itertools.combinations(array, r))


#Exibir todas as combinações
# for c in combinacoes:
#     print(c)
# resultado = ""
# for c in combinacoes:
#     resultado += "".join(c)
#
# print(resultado)




