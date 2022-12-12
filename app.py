from relatorio import relatorio

import random

index = 0

print("***** Bem-Vindo ao Gerador de Senhas! *****\n")

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*.0123456789"

numero = int(input("Quantas senhas você deseja gerar? "))

tamanho = int(input("Insira o tamanho da senha: "))

print("Aqui estão suas senhas:\n")

for x in range(numero):
    senhas = " "
    for y in range(tamanho):
        senhas += random.choice(letras)
    relatorio(index,senhas)
    index+=1