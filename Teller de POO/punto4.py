class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def HacerRuido(self):
        print("*Sonido de animal*")
        
nombre = input("Ingrese el nombre del animal \n")
edad = input("Ingrese la edad del animal \n")

mi_animal = Animal(nombre, edad)

#mi_animal = Animal("Lucas", 5)

mi_animal.HacerRuido()