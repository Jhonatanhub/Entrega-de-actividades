class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def ObtenerNombreCompleto(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        
nombre = input("Ingrese su nombre \n")
apellido = input("Ingrese su apellido \n")
edad = input("Ingrese su edad \n")

nombre_completo = Persona(nombre, apellido, edad)

# nombre_completo = Persona("Jhonatan", "Usuga", 19)

nombre_completo.ObtenerNombreCompleto()
        