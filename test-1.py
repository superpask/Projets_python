from turtle import clear


import os
os.system('cls' if os.name == 'nt' else 'clear')


def sum(a, b):
    return (a + b)

a = int(input('Entrer 1er chiffre: '))
b = int(input('Entrer 2e chiffre '))

print(chr(27) + "[2J") # escape sequence - ou clear screen

print(f'Somme de {a} et {b} égal {sum(a, b)}')
print("bravo laurent".upper())