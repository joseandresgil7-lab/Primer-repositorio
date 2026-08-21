import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Ingrese la longitud de la contraseña: "))


for j in range(20):
    contraseña_generada = ""
    for i in range(longitud):
        contraseña_generada += random.choice(caracteres)
    print("Contraseña generada:", contraseña_generada)




