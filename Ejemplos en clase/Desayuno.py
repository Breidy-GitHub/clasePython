leche=input("¿Trajo la leche? \n Digite s o n \n")
pan=input("¿Trajo la pan? \n Digite s o n \n")
huevos=input("¿Trajo la huevos? \n Digite s o n \n")
#Mama estricta
if leche=="s" and pan=="s" and huevos=="s":
    print("Agradezca que hoy desayuna")
else:
    print("Pringramoza remojada en agua")
#Mama compresiva
if leche=="s" or pan=="s" or huevos=="s":
    print("Buenos mi amor")
else:
    print("Ayy me va tocar ir a mi")