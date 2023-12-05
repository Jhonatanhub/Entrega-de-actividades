def CalcularMedia(num1, num2, num3):
    resultado = num1 + num2+ num3
    media = resultado / 3
    print("La media aritmética de los 3 números ingresados es: " , media)

num1 = int(input("Ingrese el primer número \n"))
num2 = int(input("Ingrese el segundo número \n"))
num3 = int(input("Ingrese el tercer número \n"))
CalcularMedia(num1, num2, num3)
