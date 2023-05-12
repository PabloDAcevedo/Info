# EJERCICIO 1
nombre = input("¿Cual es tu nombre?\n")
print(nombre)

# EJERCICIO 2
nombre = input("¿Cual es tu nombre?\n")
print(f"Bienvenido {nombre}")

# EJERCICIO 3
edad = input("Indique su edad:\n")
print(edad)

# EJERCICIO 4
num_1 = float(input("Ingrese un numero: \n"))
num_2 = float(input("Ingrese otro numero: \n"))
print(num_1 + num_2)

# EJERCICIO 5
num_1 = int(input("Ingrese un numero: \n"))
num_2 = int(input("Ingrese otro numero: \n"))
cociente = num_1 % num_2
resto = num_1 / num_2
print("El cociente es: ", cociente, " y el resto: ", resto)

# EJERCICIO 6
radio = float(input("Ingresa el radio del circulo: \n"))
area = 3.1416 * radio ** 2
print("El area del ciruclo es: ", area)

# EJERCICIO 7
base = float(input("Ingresa la base del triangulo: \n"))
altura = float(input("Ingresa la altura del triangulo: \n"))
area = base * altura / 2
print("El area del triangulo es: ", area)

# EJERCICIO 8
radio = float(input("Ingresa el radio del circulo: \n"))
area = 3.1416 * radio ** 2
diametro = radio * 2
circunferencia = diametro * 4.1416
print("El area del ciruclo es: ", area, "; el diametro es: ", diametro, "; y la circunferencia es: ", circunferencia)

# EJERCICIO 9
num_1 = float(input("Ingrese un numero: \n"))
num_2 = float(input("Ingrese otro numero: \n"))
multiplicacion = num_1 * num_2
suma = num_2 + num_1
resta = num_1 - num_2
division = num_1 / num_2
print("Las operaciones de los numeros son, suma=", suma, ", resta=", resta, ", multiplicacion=", multiplicacion, ", division=", division)

# EJERCICIO 10
cantidad_dolares = float(input("Ingrese la cantidad de dolares a convertir: \n"))
conversion = cantidad_dolares * 0.84
print("La cantidad de euros equivalente es: ", conversion)

# EJERCICIO 11
palabra = input("Ingrese una palabra: \n")
print("La cantidad de letras que contiene esta palabra es: ", len(palabra))

# EJERCICIO 12
fecha_nacimiento = input("Ingrese su fecha de nacimiento con este fomato: 'dd/mm/aaaa' \n")
dia,mes,anio = fecha_nacimiento.split("/")
edad = 2023 - int(anio)
print(edad)

# EJERCICIO 13
nombre = input("Ingrese su nombre: \n")
edad = int(input("Ingrese su edad: \n"))
edad += 10
print("Su edad en 10 años sera: ", edad)

# EJERCICIO 14
numero = int(input("Ingrese un numero: \n"))
print("el doble del numero es: ", numero*2, ", y el trile es: ", numero*3)

