class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def HacerRuido(self):
        print("*Sonido de animal*")
        
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    def HacerRuido(self):
        print("Guau guau")
        
nombre = input("Ingrese el nombre del perro \n")
edad = input("Ingrese la edad del perro \n")
raza = input("Ingrese la raza del perro \n")

mi_animal = Perro(nombre, edad, raza)

#mi_animal = Perro("Lucas", 5, "Labrador")

mi_animal.HacerRuido()