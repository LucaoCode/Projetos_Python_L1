# O usuário ira entrar com um texto e uma letra
# contrar a quantidade de letras aparece no texto

texto = input("Seu texto:")
letra = input("Qual a letra:")
frequencia = 0
for i in texto:
    if i == letra:
        frequencia += 1
print(f"A letra aparece {frequencia} no texto ")
