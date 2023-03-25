from salud1 import Persona

class Inicio:
    
    def __init__(self):
        self.persona1 = Persona("", "", "", "", 0, 0, 0, "")
        self.persona2 = Persona("", "", "", "", 0, 0, 0, "")
    def iniciar(self):
        print("Ingrese los datos de la persona 1:")
        self.persona1.pedirDatos()
        
        print("Ingrese los datos de la persona 2:")
        self.persona2.pedirDatos()
        
        print("\nDatos de la persona 1:")
        self.persona1.mostrarPersona()
        print("\nDatos de la persona 2:")
        self.persona2.mostrarPersona()
        
        print("\nIMC(Índice de Masa Corporal) de la persona 1: {:.2f}".format(self.persona1.calcularImc()))
        if self.persona1.calcularImc() < 20:
            print("El peso está por debajo de lo ideal")
        elif self.persona1.calcularImc() >= 20 and self.persona1.calcularImc() <= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")
        
        print("\nIMC(Índice de Masa Corporal) de la persona 2: {:.2f}".format(self.persona2.calcularImc()))
        if self.persona2.calcularImc() < 20:
            print("El peso está por debajo de lo ideal")
        elif self.persona2.calcularImc() >= 20 and self.persona2.calcularImc() <= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")
        
        print("\nPersona 1:")
        self.persona1.mayorEdad()
        print("\nPersona 2:")
        self.persona2.mayorEdad()

inicio = Inicio()
inicio.iniciar()


