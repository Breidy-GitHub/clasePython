count=0 #Definir variable numerica e inicializar antes del ciclo
total=0

for i in range(0,6):
    #Aqui instrucciones que desea repetir
    price=int(input("Ingrese el precio del producto:\n"))
    cantidad=int(input("Ingrese la cantidad del producto: "))
    count=count+1 #Inciair el contador dentro del ciclo
    subtotal=price*cantidad #Calculo del sub total
    print("Subtotal",subtotal)
    total=total+subtotal
    
print("El total a pagar es: ", total)
pago=int(input("Ingrese el pago: "))
cambio=pago-total
print("Su cambio es",cambio)

print("Cuenta con telefonia exito")
answer=input("Responda si o no: ")
if answer=="si":
    print("Usted obtuvo la cantidad de minutos: ", count)
if answer =="no":
    print("Suscribete a MobileExito")
    

#print("Se registraron",count,"Referencias")