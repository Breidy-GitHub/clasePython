# Creamos un diccionario para almacenar los competidores y sus tiempos
competidores = {}

# Solicitamos el registro de los competidores
while True:
    nombre = input("Ingrese el nombre del competidor (o escriba 'fin' para terminar): ")
    if nombre == "fin" or nombre == "Fin":
        break
    competidores[nombre] = 0.0

# Solicitamos los tiempos de cada competidor
for nombre in competidores:
    tiempo = float(input(f"Ingrese el tiempo de {nombre}: "))
    competidores[nombre] = tiempo

# Mostramos los tiempos de cada competidor
print("Tiempos de los competidores:")
for nombre, tiempo in competidores.items():
    print(nombre, tiempo)

# Determinamos el ganador
mejor_tiempo = min(competidores.values())
ganadores = [nombre for nombre, tiempo in competidores.items() if tiempo == mejor_tiempo]
if len(ganadores) == 1:
    print(f"El ganador es {ganadores[0]} con un tiempo de {mejor_tiempo}.")
else:
    print(f"Hubo un empate entre {', '.join(ganadores)} con un tiempo de {mejor_tiempo}.")
