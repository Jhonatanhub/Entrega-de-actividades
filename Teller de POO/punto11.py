class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def CalcularArea(self):
        area = self.ancho * self.alto
        print(f"El área de la forma es: {area}")
        
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def CalcularPerimetro(self):
        perimetro = (2 * self.ancho) + (2 * self.alto)
        print(f"El perimetro del rectángulo es: {perimetro}")
        
ancho = float(input("Ingrese el ancho del rectángulo \n"))
alto = float(input("Ingrese el alto del rectángulo \n"))
perimetro = Rectangulo(ancho, alto)
perimetro.CalcularPerimetro()
