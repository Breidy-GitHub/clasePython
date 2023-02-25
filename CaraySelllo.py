import random
#Entrada
print("Hola usuario, el juego comenzara en breve....")
user=input("Usuario, por favor digite si selecciona Cara o Sello: \n")
rand=random.randint(1,2)

#Operaciones
if rand==1:
    rand="Cara"
elif rand==2:
    rand="Sello"
if rand==user:
    print("Eres el ganador \n","Selio",rand)
else:
    print("Eres el perdedor \n","Salio",rand)

    


