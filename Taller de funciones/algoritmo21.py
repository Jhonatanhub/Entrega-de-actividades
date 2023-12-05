def CadenaPolindroma(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
palabra = input("Ingrese una palabra en minúscula para saber si es políndroma \n")
print(CadenaPolindroma(palabra))