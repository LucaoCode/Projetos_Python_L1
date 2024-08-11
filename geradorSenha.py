# Objetivo: Gerar uma senha segura
# usuário poderá selecionar a quantidade de caracteres aléatorios
# Salvará a senha em um arquivo 

import string 
import random
import time # para gerar o arquivo 

maiuscula = string.ascii_uppercase
minuscula = string.ascii_lowercase
digitos = string.digits
pontos = string.punctuation
tamanhoSenha = int(input("Digite o tamanho da senha: "))

senha = random.sample(maiuscula + minuscula + digitos + pontos,k=tamanhoSenha)
senha_segura = "".join(senha)
print(f"Senha gerada: {senha_segura}" )

# gerando o arquivo com a senha que será guardada
with open('senha.txt', 'a') as file:
    file.write(f"Log: {time.ctime()} - Senha: {senha_segura}\n")          
