budget=int(input("Ingrese su presupuesto: \n"))
contin=input("Si desea realizar un presione S o presione N para finalizar: ")
cont=0

while contin=="S":
    cont+=1
    if cont ==4:
        print("Recuerde que solo puede realizar 3 compras")
        break
    bills=int(input("Ingrese el valor del producto: \n"))
    contin=input("Si desea realizar un presione S o presione N para finalizar: ")
    budget=budget-bills
    print("Su gasto fue de: ",bills, "y ahora su presupuesto es de: ", budget)
    
else:
    print("Su gasto fue de: $",bills, "y ahora su presupuesto es de: $", budget)
    print("Gracias por comprar")
