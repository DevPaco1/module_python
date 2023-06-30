'''1. Escribe un script que le pregunte al usuario varios nombres 
    hasta que el usuario especifique que ya no desea ingresar más nombres.
    Como resultado deberá mostrar al usuario una lista, 
    una tupla y un set con todos los nombres que ingresó el usuario'''

lista_nombres = []
nombres = True
while nombres != False:
    nombres = input('Escribe los nombres que quieres agregar \ny escribe: "terminado" cuando ya no quieras agregar: ')
    if nombres != 'terminado':
     lista_nombres.append(nombres)
    else:
       nombres = False

tupla_nombres = tuple(lista_nombres) 
set_nombres =set(lista_nombres)
print(lista_nombres,tupla_nombres,set_nombres)

'''2. Escribe un script que calcule la diferencia entre un número dado y 17 e imprima el resultado.
    Si el número es más grande que 17 deberá imprimir el doble de la diferencia entre ambos números'''

numero_dado = float(input('Escriba un numero: '))
if numero_dado < 17 :
    resultado = 'La diferencia entre tu numero y 17 es:',numero_dado-17
else:
    resultado = 'El doble de la diferencia con el num 17 es:',(numero_dado-17)*2

print(resultado)

'''3. Escribe un script que calcule la suma de 3 números dados por el usuario.
    Si los valores son iguales deberá imprimir la suma multiplicada por 3'''

contador = 0
total_numeros = []
suma = 0
while contador < 3:
    numero_a_sumar = float(input('Esribe un numero'))
    contador += 1
    total_numeros.append(numero_a_sumar)
for numero in total_numeros:
    suma += numero
set_numeros =set(total_numeros)
if len(set_numeros) <=1:
    multiplicacion = suma*3
    print(multiplicacion)
else:
    print(suma) 

'''4. Escribe un script que calcule cuantas veces se
repite un nombre en una lista de nombres determinada
por el usuario.'''

lista_nombres = []
nombres = True
while nombres != False:
    nombres = input('Escribe los nombres que quieres agregar \ny escribe: "terminado" cuando ya no quieras agregar: ')
    if nombres != 'terminado':
     lista_nombres.append(nombres)
    else:
       nombres = False

nombre_identificado = ''
for nombre in lista_nombres:
    if nombre == nombre_identificado:
       continue
    duplicado = lista_nombres.count(nombre)
    if duplicado > 1:
        print('El nombre',nombre,'se repite',duplicado)    
        nombre_identificado = nombre


'''5. Escribe un script que determine si una letra es vocal o no'''

letra = input('Escribe una letra')
lista_letras = ['a','e','i','o','u','A','E','I','O','U']
if letra in lista_letras:
    print(f'La letra {letra} es una vocal')
else:
    print(f'La letra {letra} no es una vocal')
    


'''6. Escribe un script que detemine si un nombre dado por el usuario se encuentra en una lista de nombres. 
    La lista puede ser predeterminada o determinada por el usuario'''

lista_nombres = []
nombres = True
while nombres != False:
    nombres = input('Escribe los nombres que quieres agregar \ny escribe: "terminado" cuando ya no quieras agregar: ')
    if nombres != 'terminado':
     lista_nombres.append(nombres)
    else:
       nombres = False

nombre = input('Escriba un solo nombre')
if nombre in lista_nombres:
    print(f'El nombre {nombre} ya esta en la lista de nombres')
else:
    print(f'El nombre {nombre} no esta en la lista')

'''7. Escribe un script que le pida al usuario un número mínimo y 
    un número máximo de un rango de números.
    El script debe imprimir cuales de ellos son divisibles entre 3'''

minimo = int(input('Escribe el numero minimo de tu rango: '))
maximo = int(input('Escribe el numero maximo de tu rango: '))

for elemento in range(minimo, maximo):
    operacion = elemento % 3
    if operacion == 0:
        print(f'El numero "{elemento}" dentro de tu rango es divisible entre 3')


'''8. Escribe un script que convierta una cantidad de 
segundos dada por el usuario a horas, minutos y segundos.'''

segundos = int(input('Escribe la cantidad de segundos: '))
minutos = segundos/60
horas = minutos/60
print(f'Los segundos {segundos} son:')
print(minutos,'minutos')
print(horas, 'horas')

'''9 Escribe un script que imprima si un string dado por el usuario contiene números o no.'''

string = input('Escribe cualquier texto: ')
number = ['1','2','3','4','5','6','7','8','9','0']
for letra in string:
    if letra in number:
        print(f'El caracter "{letra}" es un numero')


