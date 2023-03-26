import random

opciones = ["piedra", "papel", "tijeras"]

print("¡Bienvenido al juego de Piedra, Papel o Tijeras!\n")

while True:
    jugador = input("Elija su opción (piedra, papel, tijeras): ").lower()
    
    if jugador not in opciones:
        print("¡Opción no válida! Intente de nuevo.\n")
        continue
        
    maquina = random.choice(opciones)
    print(f"\nLa máquina eligió: {maquina}\n")
    
    if jugador == maquina:
        resultado = "Empate"
    elif (jugador == "piedra" and maquina == "tijeras") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijeras" and maquina == "papel"):
        resultado = "Ganaste"
    else:
        resultado = "La máquina gana"
        
    print(f"{resultado}!\n")
    
    jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez != "s":
        break
        
print("\n¡Gracias por jugar!")
