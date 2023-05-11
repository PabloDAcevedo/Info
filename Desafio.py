'''
Desafio 2: Analizador de textos
Requisitos tecnicos:
Se te pide crear un programa que le pida al usuario que ingresar un texto
cualquiera, por ejemplo, un articulo o una frase.
Luego el programa le va a pedir al usuario que tambien ingrese 3 letras a su
eleccion.
Nuestro codigo va a procesar esa informacion para realizar los analisis
necesarios para devolverle al usuario la siguiente informacion:
1- Cantidad de veces que aparece cada una de letras que eligio.
Tip 1: almacenar las letras en una lista para usar algun metodo de contar un substring en un
string
Tip 2: al buscar las letras puede haber mayuscula y minusculas. Para asegurar que se
encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
minuscula.
2- Cuantas palabras hay en total en todo el texto.
Tip 3: usa metodos para transformar el texto en lista de palabras y para calcular su longitud.
3- Cual es la primera letra y cual es la ultima. (Indexacion)
4- Mostrar el texto en orden inverso.
5- Decir si la palabra "python" aparece en el texto.
Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
string para mostrar al usuario.
'''

frase = input('Ingrese una frase:').lower().strip()
letra1 = input ('Ingrese una letra:').lower()
letra2 = input ('Ingrese una letra:').lower()
letra3 = input ('Ingrese la ultima letra:').lower()

count_letra1 = frase.count(letra1)
count_letra2 = frase.count(letra2)
count_letra3 = frase.count(letra3)

count_palabras = len(frase.split(" "))
primera_letra = frase[0]
ultima_letra = frase[-1]
texto_inverso = frase [::-1]
texto_orden_inverso = frase.split(" ")[::-1]
texto_orden_inverso2= " ".join (texto_orden_inverso)

print("el numero de veces que tu letra aparece en la frase es: ","\n", letra1,"=", count_letra1,"\n", letra2,"=", count_letra2,"\n", letra3,"=", count_letra3)
print("En el texto hay un total de: ",count_palabras,"palabras")
print("La primera letra de la frase es: '",primera_letra,"' y la ultima es '",ultima_letra, "'")
print("su texto en forma inversa es:",texto_inverso)
print (texto_orden_inverso2)

if "python" in frase:
    print("La palabra python SI se encuentra en la frase")
else:
    print ("La palabra python NO se encuntra en la frase")


#GRUPO 11 - INTEGRANTES 
# Joel Chavez
# Renzo Arrieta
# Pablo Acevedo
# Serial Trachta Matias Gaston
# Lugo Mauro Rodrigo
# Julio R. Escanciano Gonzalez
# Facundo Vicedo
# Gabriel Leiva
# Maximiliano Imanol Aguer
# Salto Cristian J.














