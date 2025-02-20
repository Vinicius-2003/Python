import os


times_brasileirao = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco da Gama",
    "Vitória",
    "Atlético Mineiro",
    "Fluminense",
    "Grêmio",
    "Juventude",
    "Red Bull Bragantino",
    "Athletico Paranaense",
    "Criciúma",
    "Atlético Goianiense",
    "Cuiabá"
)

os.system('cls')

# Apenas os primeiros 5 colocados
print(f"Os 5 primeiros times da tabela : {times_brasileirao[:5]}")

# Apenas os 4 últimos
print(f"Os últimos 4 colocados da tabela : {times_brasileirao[0:-4]}")

# Lista ordenada em ordem alfabética
print(f" A lista ordenada em ordem alfabética : {sorted(times_brasileirao)}")

# Em que posição está  o Criciúma na tabela
for time in times_brasileirao:
    if time == "Criciúma":
        print(f"O Criciúma está na {times_brasileirao.index("Criciúma")+1} posição")
        