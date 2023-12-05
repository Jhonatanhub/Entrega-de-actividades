def CalcularFactorial(numero):
    factorial = 1
    if numero > 100 and numero <= 1000:
        for i in range(1,numero + 1):
            factorial = factorial * i
            print("El factorial del número ingresado es: " , factorial)        
    elif numero > 0 and numero < 100:
        print("El número ingresado está por debajo del rango esperado")
    else:
        print("El número está por encima del rango esperado")
           
numero = int(input("Ingrese un número entre 100 y 1.000 \n"))
CalcularFactorial(numero)
