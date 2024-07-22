h = 1
m = 0

Obter_hora = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}

numeros_texto = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three",
    "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight",
    "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four",
    "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine",
    "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five",
    "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty", "fifty-one",
    "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven",
    "fifty-eight", "fifty-nine"
]

numeros_dict = {i: numeros_texto[i] for i in range(60)}
minutes_text = numeros_dict.get(m)
nova_hora = Obter_hora.get(h)

if 0 <= m <= 30:
    if m == 0:
        print(nova_hora + " " + "o'clock")
    elif m == 1:
        print(minutes_text + " " + "minute" + " " + "past" + " " + nova_hora)
    elif m == 15:
        print("quarter" + " " + "past" + " " + nova_hora)
    elif m == 30:
        print("half" + " " + "past" + " " + nova_hora)
    else:print(minutes_text + " " + "minutes" + " " + "past" + " " + nova_hora)
else:
    if m == 45:
        h = h + 1
        nova_hora = Obter_hora.get(h)
        print("quarter" + " " + "to" + " " + nova_hora)
    elif h == 12:
        m = 60 - m
        minutes_text = numeros_dict.get(m)
        print(minutes_text + " " + "minutes" + " " + "to" + " " + "one")
    else:
        m = 60 - m
        h = h + 1
        nova_hora = Obter_hora.get(h)
        minutes_text = numeros_dict.get(m)
        print(minutes_text + " " + "minutes" + " " + "to" + " " + nova_hora)


