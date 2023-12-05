def DivisionyResto(dividendo, divisor):
    if dividendo < divisor:
        return 0, dividendo
    else:
        cociente, resto = DivisionyResto(dividendo - divisor, divisor)
        return cociente + 1, resto

dividendo = int(input("Ingrese el numero dividendo \n"))
divisor = int(input("Ingrese el numero divisor \n"))
cociente, resto = DivisionyResto(dividendo, divisor)
print(f"El resultado de la división es {cociente}")
print(f"El resto de la división es {resto}")