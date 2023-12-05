class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        
    def CalcularSalarioNeto(self, impuestos, otros_descuentos):
        salario_neto = self.sueldo - impuestos - otros_descuentos
        print(f"El salario neto del empleado es: {salario_neto}")

nombre = input("Ingrese el nombre del empleado \n")
apellido = input("Ingrese el apellido del empleado \n")
sueldo = float(input("Ingrese el sueldo del empleado \n"))
impuestos = float(input("Ingrese el valor de los impuestos que paga el empleado \n"))
otros_descuentos = float(input("Ingrese el valor de otros descuentos que paga el empleado \n"))        
salario = Empleado(nombre, apellido, sueldo)
salario.CalcularSalarioNeto(impuestos, otros_descuentos)