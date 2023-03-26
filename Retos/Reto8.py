# Solicitamos las notas al usuario y las almacenamos en una lista
notas = []
while True:
    nota = input("Ingrese una nota entre 0.0 y 5.0 (o escriba 'fin' para terminar): ")
    if nota == "fin":
        break
    try:
        nota = float(nota)
        if nota < 0.0 or nota > 5.0:
            print("La nota debe estar entre 0.0 y 5.0.")
        else:
            notas.append(nota)
    except ValueError:
        print("Debe ingresar un número o la palabra 'fin'.")

# Calculamos el promedio de las notas y mostramos el resultado
if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print("Su nota final es:", promedio)
    # Agregamos las anotaciones según corresponda
    if promedio < 3.0:
        print("Reprobaste.")
    elif promedio < 4.0:
        print("Pasaste raspando.")
    else:
        print("Aprobaste con buenos resultados.")
else:
    print("No ingresó ninguna nota.")
