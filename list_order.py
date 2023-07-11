# Escribir un script que permita ordenar la siguiente lista de tuplas por el segudo valor de cada tupla
# de manera ascendente y descendente

pair_numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


 
def get_second_value(tupla):
    return tupla[1]

pair_numbers.sort(key=get_second_value)
print('Orden ascendete: ', pair_numbers)
pair_numbers.sort(key=get_second_value, reverse=True)
print('Orden descendente: ', pair_numbers)

    

