class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def CalcularArea(self):
        area = self.ancho * self.alto
        print(f"El área de la forma es: {area}")
        
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def CalcularCircunferencia(self):
        circunferencia = 2 * 3.14 * self.radio
        print(f"La circunferencia del circulo es: {circunferencia}")
        
radio = float(input("Ingrese el radio del circulo \n"))
circulo = Circulo(radio)
circulo.CalcularCircunferencia()