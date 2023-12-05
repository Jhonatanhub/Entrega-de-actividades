import math

def ConversionCoordenadas(r, theta):
    theta_radianes = math.radians(theta)
    
    x = r * math.cos(theta_radianes)
    y = r * math.sin(theta_radianes)
    
    print(f"Las coordenadas cartesianas correspondientes son: x = {x}, y = {y}")

r = float(input("Ingrese la magnitud de r \n"))
theta = float(input("Ingrese el valor del ángulo \n"))

ConversionCoordenadas(r, theta)
