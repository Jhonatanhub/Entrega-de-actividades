class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def ObtenerNombreCompleto(self):
        print(self.nombre, self.apellido)
        
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
        
    def ObtenerNombreCompleto(self):
        print(f"Nombre: {self.nombre} {self.apellido} \nCarrera: {self.carrera}")
        
nombre = input("Ingrese su nombre \n")
apellido = input("Ingrese su apellido \n")
edad = input("Ingrese su edad \n")
carrera = input("Ingrese la carrea que está estudiando \n")

nombre_completo = Estudiante(nombre, apellido, edad, carrera)

# nombre_completo = Estudiante("Jhonatan", "Usuga", 19, "Análisis y desarrollo de software")

nombre_completo.ObtenerNombreCompleto()
        