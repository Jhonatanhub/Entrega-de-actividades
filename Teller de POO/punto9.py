class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def ObtenerNombreCompleto(self):
        print(self.nombre, self.apellido)
        
class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.materia = materia
        
    def ObtenerNombreCompleto(self):
        print(f"Nombre: {self.nombre} {self.apellido} \nMateria: {self.materia}")
        
nombre = input("Ingrese su nombre \n")
apellido = input("Ingrese su apellido \n")
edad = input("Ingrese su edad \n")
materia = input("Ingrese la materia que está dando \n")

nombre_completo = Profesor(nombre, apellido, edad, materia)

# nombre_completo = Profesor("Jhonatan", "Usuga", 19, "Inglés")

nombre_completo.ObtenerNombreCompleto()