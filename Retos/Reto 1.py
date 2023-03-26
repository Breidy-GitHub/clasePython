countFame=0
countMale=0

for i in range(0,10):
    answer=input("Responda Hombre o Mujer: ")
    if answer=="Hombre":
        countMale+=1
    else:
        countFame+=1
print("El total de Mujeres es: ",countFame, "El total de Hombes es: ",countMale)

