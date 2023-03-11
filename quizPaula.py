# Definimos las constantes de valor de entrada
EXTRANJEROS = 60000
NACIONALES = 32000

# Pedimos la cantidad de visitantes de cada tipo
extranjeros = int(input("¿Cuántos extranjeros visitaron el parque Tayrona? "))
nacionales = int(input("¿Cuántos nacionales visitaron el parque Tayrona? "))

# Calculamos el total recaudado
totalEx= (extranjeros * EXTRANJEROS)
totalNa=(nacionales * NACIONALES)

# Mostramos el resultado
print("Total de Extranjeros es: ", totalEx)
print('Total de Nacionales es: ', totalNa)






