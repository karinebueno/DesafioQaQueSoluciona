n = 4
contador = 0

for element in range(n):
    contador = contador + 1
    hashtag = ""
    for i in range(contador):
        hashtag = hashtag + "#"
        espaco = ""
    for _ in range(n - contador):
        espaco = espaco + " "
    print(espaco + hashtag)
