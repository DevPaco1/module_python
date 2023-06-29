'''#exercise 1
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


#exercise 2
print('\n')


nombre = input('Escibe tu primer nombre: ')
apellido = input('Escribe tu primer apellido: ')
edad = int(input('Escribe tu edad: '))
calculo_edad = str(edad-2023)

print('Hola',nombre,apellido + ',','naciste en',calculo_edad[-4:])

#Exercise 3
print('\n')

radio = int(input('Escribe el radio de un circulo: '))
pi = 3.1416
calculo_area = pi * (radio**2)

print('El ares del circulo es:',calculo_area)

#Exercise 4
print('\n')

numero = input('Escribe un numero: ')
print('la suma de:',numero,"+",numero*2,'+',numero*3,'=',int(numero)+int(numero*2)+int(numero*3))

#Exercise 5'''


print('Escribe un numero')
numero = input(float())
if numero == input(float()):
        if numero % 2 == 0 :
                print(numero,'es par')
        else :
                print(numero,'es impar')
else:
    print('Escribe un digito')

while numero != int():
    print('escribe un digito')
    numero = input(int())
    print('gracias')
       

'''print('what is your age?')
myAge = input(int())
 
if myAge == input(int()):
    print('thank you')
else:
    print('please enter the number only')
 
while myAge != int():
    print('please enter the number only')
    myAge = input(int())
print('thank you')'''
'''#Exercise 6
print('\n')

base = int(input('Escribe la base del triangulo: '))
altura = int(input('Escribe la altura del triangulo: '))'''

