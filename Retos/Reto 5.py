import random

print("¡Bienvenido a la promoción de aniversario de Supermercados Noé!\n")

compra = float(input("Por favor ingrese el valor de su compra: "))

if compra > 50000:
    bolita = random.choice(["roja", "azul", "amarilla", "blanca"])
    print(f"\nFelicidades, ha obtenido una bolita {bolita}.\n")
    
    if bolita == "roja":
        descuento = 0.1
    elif bolita == "azul":
        descuento = 0.3
    elif bolita == "amarilla":
        descuento = 0.5
    else:
        descuento = 1.0
    
    valor_final = compra * (1 - descuento)
    print(f"Su descuento es del {descuento*100:.0f}%, y su valor final a pagar es de ${valor_final:.2f}")
    
else:
    print("Lo siento, su compra no es elegible para esta promoción.")
    
print("\n¡Gracias por comprar en Supermercados Noé!")
