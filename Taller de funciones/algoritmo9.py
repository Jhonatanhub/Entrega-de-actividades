def Digito(numero):
    if numero >= 0 and numero < 10:
        return True
    else:
        return False
    
numero = int(input("Ingrese un número para saber si está dentro del rango \n"))
print(Digito(numero))