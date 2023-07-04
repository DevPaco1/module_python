#1.-Escribe una función qué reciba varios números y devuelva el mayor de ellos.
'''def Numero_Mayor(lista_numeros):
    lista_numeros.sort()
    resultado = print(f'El numero mayor es: "{lista_numeros[-1]}"')
    return resultado

numeros = True
lista_numeros = []
while numeros != False:
    numeros = input('Escribe un numero y para ya no agregar escribe n: ')
    escape = ['n','N','NO','no','No','nO']
    if numeros not in escape:
        numeros_float = float(numeros)
        lista_numeros.append(numeros_float)
    else:
        numeros = False
Numero_Mayor(lista_numeros)   '''    
#2.-Escribe una función que permita multiplicar varios números

'''def Multiplicar (numero1,numero2):
    resultado = print(numero1*numero2)
    return resultado

numero1 = float(input('Escribe el primer numero: '))
numero2 = float(input('Escribe el segundo numero: '))

Multiplicar(numero1,numero2)'''

#3.-Escribe una función para verificar que un número se encuentra en un rango de números determinado. 
#El resultado de esa función debe ser booleano

'''def Existente(numero,rango):
    if numero in rango:
        resultado = print(True)
    else:
        resultado= print(False)
    return resultado
rango = range(1,20)
numero = int(input('Escribe un numero: '))

Existente(numero,rango)'''


#4.-Escribe una función que permita identificar si un número dado es primo o no.

'''def Primo(numero):
    if numero % 2 and numero // numero:
         print('El numero es primo')
    else:
         print('El numero no es Primo')
Primo(int(10))'''

#5.-Escribe un programa que pueda identificar si una palabra o 
#frase es un palíndromo (https://es.wikipedia.org/wiki/Pal%C3%ADndromo).

'''def palindromo(palabra):
    palabra_list = list(palabra)
    palabra_reversa = palabra_list[::-1]
    if palabra_list == palabra_reversa:
        print('La palabra es un palindromo')
    else:
        print('La palabra no es un palindromo')
    print(palabra_list)
    print(palabra_reversa)

palabra = input('Escribe una palabra: ')
palindromo(palabra)'''

#6.-Escribe una función que genere una lista con los números de la serie de fibonacci.
#La función debe recibir la cantidad de números a generar


'''def fibonacci(numero):
    contador = 2
    list_fibonacci =[1,1]
    while contador != numero:
        suma_fibonacci = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(suma_fibonacci)
        contador += 1
    return print(list_fibonacci)

numero = int(input('Escribe un numero: '))
    
fibonacci(numero)'''


#7.-Escribe un programa que emule el funcionamiento de una calculadora simple. 
#Este es un posible ejemplo de la ejecución del programa en una terminal:
init = True
cosiente = []
while init != False:
    instrucciones = input()
    if instrucciones != '=' :
        list_instrucciones = list(instrucciones)
        if len(list_instrucciones)<=1:
            cosiente1 = list_instrucciones[0]
            cosiente.append(int(cosiente1))
            print(cosiente)
        else:
            cosiente2 = list_instrucciones[1]
            cosiente.append(int(cosiente2))

            operador = list_instrucciones[0]
            if operador == '+':
               operacion = cosiente[-1] + cosiente[-2]
            elif operador == '-':
                operacion = cosiente[-2] - cosiente[-1]
            elif operador == '*':
                operacion = cosiente[-1] * cosiente[-2]
            else:
                operacion = cosiente[-2] / cosiente[-1]

            
            cosiente.append(operacion)
            print(operacion)
    else:
        init = False
print(cosiente)





'''8.- Escribe un programa tipo "Caja registradora", que 
permita introducir una lista de artículos, cantidad y precio. 
Al final debe mostrarle al usuario la cantidad de artículos y la cantidad a cobrar (editado) '''