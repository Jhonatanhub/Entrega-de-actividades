class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def ObtenerInfo(self):
        print(f"La información del vehículo es: \n Marca: {self.marca} \n Modelo: {self.modelo} \n Año: {self.ano}")
        
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, ano, capacidad_carga):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidad_carga = capacidad_carga
        
    def ObtenerInfo(self):
        print(f"La información del vehículo es: \nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.ano} \nCapacidad de carga: {self.capacidad_carga} kg")      
        
marca = input("Ingrese la marca de la camioneta \n")
modelo = input("Ingrese el modelo de la camioneta \n")
ano = input("Ingrese el año de la camioneta \n")
capacidad_carga = input("Ingrese la capacidad de carga de la camioneta \n")

mi_vehiculo = Camioneta(marca, modelo, ano, capacidad_carga)

#mi_vehiculo = Camioneta("Toyota", "4*4", 2023, 90)

mi_vehiculo.ObtenerInfo()