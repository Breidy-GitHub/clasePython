from Persona import Persona

class Empleado(Persona):
    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, cargo, valorhora, horastrabajadas, departamento):
        super().__init__(tipo_documento, numero_documento, nombres, apellidos)
        self.cargo = cargo
        self.valorhora = valorhora
        self.horastrabajadas = horastrabajadas
        self.departamento = departamento
        
    def calcularHonorarios(self):
        total_pagar = self.valorhora * self.horastrabajadas
        retencion = total_pagar * 0.00966 # 0.966%
        return total_pagar - retencion
        
    def imprimirEmpleado(self):
        print(f"Tipo de documento: {self.tipo_documento}")
        print(f"Número de documento: {self.numero_documento}")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Cargo: {self.cargo}")
        print(f"Horas trabajadas: {self.horastrabajadas}")
        print(f"Valor por hora: {self.valorhora}")
        print(f"Total a pagar: {self.calcularHonorarios()}")
