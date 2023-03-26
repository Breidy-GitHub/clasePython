import random

# Definir un valor global para apostar
valor_apostado = 10
dinero_acumulado = 0
contador_juegos = 0

# Repetir el juego las veces que el jugador lo desee
while True:
    # Posibilidad para apostar una cantidad de dinero específica (ingresada por el usuario) en cada jugada
    dinero_apostado = int(input(f"\nJuego {contador_juegos+1}: ¿Cuánto dinero desea apostar? "))
    if dinero_apostado > 0:
        # Realizar la apuesta
        contador_juegos += 1
        moneda = random.choice(["cara", "sello"])
        if moneda == "cara":
            dinero_acumulado += dinero_apostado * 2
            valor_apostado = dinero_apostado * 2
            print("¡Ganaste! La moneda mostró cara.")
        else:
            dinero_acumulado -= dinero_apostado
            valor_apostado = dinero_apostado
            print("Lo siento, perdiste. La moneda mostró sello.")
        # Mostrar el dinero acumulado y el valor apostado en el juego actual
        print(f"Dinero acumulado: {dinero_acumulado}")
        print(f"Valor apostado en este juego: {valor_apostado}")
    else:
        print("El valor apostado debe ser mayor que cero.")
    # Preguntar si el jugador desea seguir jugando
    respuesta = input("¿Desea seguir jugando? (S/N) ").lower()
    if respuesta == "n":
        break

# Al final del juego debe decirle la cantidad de veces que jugó y el dinero que acumuló.
print(f"\nJugaste {contador_juegos} veces y acumulaste un total de {dinero_acumulado} pesos.")
