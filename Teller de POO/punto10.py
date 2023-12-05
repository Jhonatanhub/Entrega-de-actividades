class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def CalcularArea(self):
        area = self.ancho * self.alto
        print(f"El área de la forma es: {area}")
        
ancho = float(input("Ingrese el ancho de la forma \n"))
alto = float(input("Ingrese el alto de la forma \n"))
area = Forma(ancho, alto)
area.CalcularArea()
        