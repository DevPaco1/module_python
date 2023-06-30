'''1. Escribe un script que imprima las primeras estrofas de la canción de la víbora de la mar con el siguiente formato:

A la víbora, víbora
	De la mar, de la mar
		Por aquí pueden pasar
	Los de adelante corren mucho
		Y los de atrás se quedarán

A la víbora, víbora
	De la mar, de la mar
		Por aquí pueden pasar
	Los de adelante corren mucho
		Y los de atrás se quedarán
		Tras, tras, tras'''

line_1 ='A la vibora, vibora\n'
line_2 ='De la mar, de la mar\n'
line_3 ='Por aqui pueden pasar\n'
line_4 ='Los de adelante corren mucho\n'
line_5 ='y los de atras se quedaran\n'
line_6 ='Tras, tras, tras'
two_spaces = '  '
four_spaces = '     '

print(line_1,two_spaces + line_2,four_spaces + line_3,two_spaces + line_4,four_spaces + line_5)
print(line_1,two_spaces + line_2,four_spaces + line_3,two_spaces + line_4,four_spaces + line_5,four_spaces + line_6)


'''2. Escribe un programa que solicite el nombre, el apellido y 
la edad del usuario e imprima un saludo y su año de nacimiento. 
Tomar el año actual como constante (2023)'''

nombre = input('Escibe tu primer nombre: ')
apellido = input('Escribe tu primer apellido: ')
edad = int(input('Escribe tu edad: '))
calculo_edad = str(edad-2023)

print('Hola',nombre,apellido + ',','naciste en',calculo_edad[-4:])

'''
3. Escribe un script que calcule el área de un círculo 
basado en el radio proporcionado por el usuario e imprima el resultado.
'''


radio = int(input('Escribe el radio de un circulo: '))
pi = 3.1416
calculo_area = pi * (radio**2)

print('El ares del circulo es:',calculo_area)

'''4. Escribe un script que solicite un número (n) y calcule el valor de n + nn + nnn'''


numero = input('Escribe un numero: ')
print('la suma de:',numero,"+",numero,'+',numero,'=',int(numero)+int(numero**2)+int(numero**3))

'''5. Escribe un script que solicite un número y devuelva notifique 
 usuario si el número es par o impar'''


print('Escribe un numero')
numero = input(float())
if numero == input(float()):
        if numero % 2 == 0 :
                print(numero,'es par')
        else :
                print(numero,'es impar')

       

'''6. Escribe un script que solicite la base y la altura de un triángulo,
 calcule su área e imprima el resultado'''


base = int(input('Escribe la base del triangulo: '))
altura = int(input('Escribe la altura del triangulo: '))
print(f'El area del triangulo es: {base*altura/2}')