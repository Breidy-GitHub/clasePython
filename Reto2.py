import random

# Entrada
print("Hola usuario, el juego comenzará en breve....")
user = input("Usuario, por favor seleccione Cara o Sello: ").lower()

# Operaciones
rand = random.choice(["cara", "sello"])
if rand == user:
    print("¡Eres el ganador!")
else:
    print("Lo siento, perdiste. La moneda mostró", rand)

