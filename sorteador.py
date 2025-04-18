import random

passeios = input("Digite os passeios a serem sorteados, separando por vírgula: ")
lista_passeios = passeios.split(",")
print(lista_passeios)
passeio_sorteado = random.choice(lista_passeios)
print(passeio_sorteado)