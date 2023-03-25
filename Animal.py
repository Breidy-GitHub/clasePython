class Animal:
    # Atributos
    nombre = ""  # Atributo
    edad = 0
    # Métodos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def registrarAnimal(self):
        self.nombre = input("Ingrese el nombre del animal: ")
        self.edad = int(input("Ingrese la edad del animal: "))
    def mostrarAnimal(self):
        print(f"El nombre del animal es {self.nombre} y la edad es {self.edad}")

panda = Animal("Bambu", 7)
guacamayo = Animal(" ", 0)

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