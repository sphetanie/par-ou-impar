# Projeto par ou ímpar

x = input(float("Escolha um número: "))

def par():
    if x%2 == 0:
        print("É par.")

def impar():
    if x%2 != 0:
        print("É ímpar.")

