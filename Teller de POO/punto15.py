class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        
    def CalcularSalarioNeto(self, impuestos, otros_descuentos):
        salario_neto = self.sueldo - impuestos - otros_descuentos
        print(f"El salario neto del empleado es: {salario_neto}")
        
class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, lenguaje):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.lenguaje = lenguaje
        
    def CalcularSalarioNeto(self, impuestos, otros_descuentos, bono):
        salario_neto = self.sueldo - impuestos - otros_descuentos + bono
        print(f"El salario neto del programador es: {salario_neto}")

nombre = input("Ingrese el nombre del programador \n")
apellido = input("Ingrese el apellido del programador \n")
lenguaje = input("Ingrese el lenguaje que maneja el programador \n")
sueldo = float(input("Ingrese el sueldo del programador \n"))
impuestos = float(input("Ingrese el valor de los impuestos que paga el programador \n"))
otros_descuentos = float(input("Ingrese el valor de otros descuentos que paga el programador \n"))    
bono = float(input("Ingrese el valor del bono adicional que recibe el programador \n")) 
    
salario = Programador(nombre, apellido, sueldo, lenguaje)
salario.CalcularSalarioNeto(impuestos, otros_descuentos, bono)