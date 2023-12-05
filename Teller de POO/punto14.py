class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        
    def CalcularSalarioNeto(self, impuestos, otros_descuentos):
        salario_neto = self.sueldo - impuestos - otros_descuentos
        print(f"El salario neto del empleado es: {salario_neto}")
        
class Gerente(Empleado):
    def __init__(self, nombre, apellido, sueldo, departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.departamento = departamento
        
    def CalcularSalarioNeto(self, impuestos, otros_descuentos, bono):
        salario_neto = self.sueldo - impuestos - otros_descuentos + bono
        print(f"El salario neto del gerente es: {salario_neto}")

nombre = input("Ingrese el nombre del gerente \n")
apellido = input("Ingrese el apellido del gerente \n")
departamento = input("Ingrese el departamento al cual pertenece el gerente \n")
sueldo = float(input("Ingrese el sueldo del gerente \n"))
impuestos = float(input("Ingrese el valor de los impuestos que paga el gerente \n"))
otros_descuentos = float(input("Ingrese el valor de otros descuentos que paga el gerente \n"))    
bono = float(input("Ingrese el valor del bono adicional que recibe el gerente \n")) 
    
salario = Gerente(nombre, apellido, sueldo, departamento)
salario.CalcularSalarioNeto(impuestos, otros_descuentos, bono)