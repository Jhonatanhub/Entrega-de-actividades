class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def ObtenerInfo(self):
        print(f"La información del vehículo es: \nMarca: {self.marca} \nModelo: {self.modelo} \nAño: {self.ano}")
        
marca = input("Ingrese la marca del vihículo \n")
modelo = input("Ingrese el modelo del vehículo \n")
ano = input("Ingrese el año del vehículo \n")

mi_vehiculo = Vehiculo(marca, modelo, ano)

#mi_vehiculo = Vehiculo("Audi", "R8", 2023)

mi_vehiculo.ObtenerInfo()
