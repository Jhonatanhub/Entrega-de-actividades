class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def HacerRuido(self):
        print("*Sonido de animal*")
        
class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        self.nombre = nombre
        self.edad = edad
        self.pelaje = pelaje
    
    def HacerRuido(self):
        print("Miau miau")
        
nombre = input("Ingrese el nombre del gato \n")
edad = input("Ingrese la edad del gato \n")
pelaje = input("Ingrese el pelaje del gato \n")

mi_animal = Gato(nombre, edad, pelaje)

# mi_animal = Gato("Lupe", 3, "jsad")

mi_animal.HacerRuido()