import random
#Entrada
dado1=random.randint(1,6)
dado2=random.randint(1,6)

#Operaciones
print("Es dado uno es: ",dado1,"\nEl dado dos es: ",dado2)

if dado1==1 and dado2==1 or dado1==6 and dado2==6:
    print("Eres el ganador")
elif dado1 + dado2==3 or dado1+dado2==11 or dado1+dado2==7:
    print("Eres el ganador")
else:
    print("Eres perdedor")

