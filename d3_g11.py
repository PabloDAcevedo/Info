from random import randint

nombre = input("Ingresar nombre: ")

print(f"""
Bienvenido {nombre}
Juego de adivina el numero.
Dato: El programa elige un numero al azar entre 1 y 100, y deberas adivinarlo.
Aviso: ¡Solo tienes 8 intentos!
""")

numero_azar = randint(1, 100)
intentos = 1

while intentos <= 8:  # Se evaluan los intentos restantes
    if intentos == 8:  
        print("¡Atencion, este es tu ultimo intento!")
    numero = input("Ingresa un numero: ")
    if numero.isdigit():  # numero sea un digito valido
        numero = int(numero) # convierte el input a int
        if numero < 1 or numero > 100:  # si el numero esta fuera del rango
            print("¡El numero debe estar entre 1 y 100!")
        else:  # si es un digito y esta dentro del rango
            if numero == numero_azar:  # si adivino el numero
                print(
                    f"¡Muy bien {nombre}! El numero es el correcto.\nLo hiciste con un total de {intentos} intentos.")
                break
            else:  # si no se adivino el numero
                if intentos == 8:  # es el ultimo intento
                    print(
                        f"¡Se termino el juego, mejor suerte la proxima vez! El numero era {numero_azar}")
                else:  # Falla e impresion de intentos
                    print(
                        f"¡Ups! intentalo de nuevo, este fue tu intento numero {intentos}\nTe quedan {8-intentos} intentos")
                    if numero > numero_azar: # se informa por pantalla si el numero es mayor o menor
                        print("El numero ingresado es mayor al que intestas adivinar\n")
                    else:
                        print("El numero ingresado es menor al que intestas adivinar\n")
                intentos += 1
    else:  # se informa por pantalla que el numero no es un digito valido
        print("¡Asegurate de ingresar un numero entero!")


# INTEGRANTES GRUPO 11
# Renzo, Arrieta
# Pablo, Acevedo
# Matías Gastón, Serial Trachta
# Lugo Mauro, Rodrigo
# Julio R, Escanciano Gonzalez
# Facundo, Vicedo
# Gabriel, Leiva
# Joel, Chavez
# Maximiliano Imanol, Aguer
# Cristian J, Salto
