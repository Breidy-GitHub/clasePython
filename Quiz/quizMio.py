azul = 0
rojo = 0

while True:
    # Pedimos al usuario que responda "Rojo" o "Azul"
    color = input("Responda Rojo o Azul (o escriba 'fin' para terminar): ")
    # Si el usuario escribe 'fin', detenemos el bucle
    if color == 'fin':
        break
    # Si el usuario escribe una respuesta válida, actualizamos el conteo correspondiente
    elif color == "Rojo"or color=='rojo':
        rojo += 1
    elif color == "Azul" or color=='azul':
        azul += 1
    # Si el usuario escribe una respuesta inválida, le pedimos que vuelva a intentarlo
    else:
        print("Respuesta inválida. Por favor, responda 'Rojo' o 'Azul'.")
        continue

print("El total de azul es:", azul, "El total de rojo es:", rojo)


