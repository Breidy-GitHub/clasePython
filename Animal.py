class Animal:
    #Atributos
    nombre="" #Atributo
    edad=0
    #Metodos
    def registraranimal(self):
        nombre=input("Ingrese el nombre del animal: ")
        edad=int(input("Ingrese la edad del animal: "))
    def mostrarAnimal(self,nombre,edad):
        #print("El nombre del animal es: ", nombre,"y la edad es: ", edad)
        print(f"El nombre del animal es: {nombre} y la edad es {edad}")
    #Definir metodo con valor de retorno
    def duplicarEdad(self,edad):
        duplicado=edad*2
        return duplicado
#Crear objeto-> Instanciar Clase
tigre=Animal()
tigre.nombre="Tony"
tigre.edad=5
print("El nombre del animal es: ",tigre.nombre,"y su edad es: ", tigre.edad )
#Invocar Metodo
tigre.registraranimal()
tigre.mostrarAnimal("Tony2",10)
duplicar=tigre.duplicarEdad(5)
print(f"La edad duplicada es: {duplicar}")