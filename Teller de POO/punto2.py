class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def ObtenerInfo(self):
        print(f"La información del vehículo es: \n Marca: {self.marca} \n Modelo: {self.modelo} \n Año: {self.ano}")
        
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ano, numero_puertas):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.numero_puertas = numero_puertas
        
    def ObtenerInfo(self):
        print(f"La información del vehículo es: \nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.ano} \nNúmero de puertas: {self.numero_puertas}")      
        
marca = input("Ingrese la marca del vihículo \n")
modelo = input("Ingrese el modelo del vehículo \n")
ano = input("Ingrese el año del vehículo \n")
numero_puertas = input("Ingrese cuántas puertas tiene el carro \n")

mi_vehiculo = Automovil(marca, modelo, ano, numero_puertas)

#mi_vehiculo = Automovil("Audi", "R8", 2023, 4)

mi_vehiculo.ObtenerInfo()