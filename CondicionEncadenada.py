edad=int(input("ingresa tu edad en años \n"))
if 0<=edad<=4:
    print("El cliente ingresa gratis")
elif 4<edad<18:
    print("El cliente debe pagar $20.000")
elif 18<=edad<=60:
    print("El cliente debe pagar $15.000")
elif edad>60:
    print("El cliente debe pagar $3000")
else:
    print("NO PUEDE INGRESAR ")