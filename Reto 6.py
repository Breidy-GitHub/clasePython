import random

print("¡Bienvenido a la promoción de aniversario de Supermercados Noé!\n")

total = 0
cantidad_productos = int(input("¿Cuántos productos va a registrar? "))

for i in range(cantidad_productos):
    precio = float(input(f"Ingrese el precio del producto {i+1}: "))
    cantidad = int(input(f"Ingrese la cantidad del producto {i+1}: "))
    total += precio * cantidad
    
if total > 50000:
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
    
    valor_descuento = total * descuento
    valor_final = total - valor_descuento
    
    print(f"Su descuento es del {descuento*100:.0f}%, y su valor final a pagar es de ${valor_final:.2f}")
    
    pago = float(input("\nIngrese con cuanto va a pagar: "))
    cambio = pago - valor_final
    
    if cambio >= 0:
        print(f"\nSu cambio es de ${cambio:.2f}")
    else:
        print("\nLo siento, no ha ingresado suficiente dinero.")
        
else:
    print("\nLo siento, su compra no es elegible para esta promoción.")
    
print("\n¡Gracias por comprar en Supermercados Noé!")
