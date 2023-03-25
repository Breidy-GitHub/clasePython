class Animal:
    #Atributos
    nombre=""
    edad=0
    #Metodos
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def registrarAnimal(self):
        self.nombre=input("Ingrese el nombre del animal: ")
        self.edad=int(input("Ingrese la edad del animal: "))
    '''def mostrarAnimal(self,nombre,edad):
        #print("El nombre del animal es: ", nombre,"y la edad es: ", edad)
        print(f"El nombre del animal es: {nombre} y la edad es {edad}")'''
    def mostrarAnimal(self):
        print(f"El nombre del animal es {self.nombre} y la edad es {self.edad}")
    #Definir metodo con valor de retorno
    def duplicarEdad(self,edad):
        duplicado=edad*2
        return duplicado
panda=Animal("Bambu",7)
guacamayo=Animal(" ",0)

guacamayo.registrarAnimal()
guacamayo.mostrarAnimal()

'''Crear objeto-> Instanciar Clase
tigre=Animal()
tigre.nombre="Tony"
tigre.edad=5
print("El nombre del animal es: ",tigre.nombre,"y su edad es: ", tigre.edad )
Invocar Metodo
tigre.registraranimal()
tigre.mostrarAnimal("Tony2",10)
duplicar=tigre.duplicarEdad(5)
print(f"La edad duplicada es: {duplicar}")'''