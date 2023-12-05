def ConvertirMayus(palabra):
    palabra = palabra.upper()
    print(palabra)

def ConvertirMinus(palabra):
    palabra = palabra.lower()
    print(palabra)
    
palabra = input("Ingrese una palabra \n")
ConvertirMayus(palabra)
ConvertirMinus(palabra)
