import os

alumno = input('nombre del alumno: ')

with open("lista.txt", "r") as archivo:
    for linea in archivo:
            if alumno in linea:
                print(linea)
            else:
                print('el alumno no está bien escrito o no está presente')