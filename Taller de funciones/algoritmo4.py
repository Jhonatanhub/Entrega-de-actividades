def CalcularNumMayor(num1, num2):
    if num1 > num2:
        print("El número mayor es el: " , num1)
    else:
        print("El número mayor es el: " , num2)
        
num1 = int(input("Ingrese el primer número \n"))
num2 = int(input("Ingrese el segundo número \n"))
CalcularNumMayor(num1, num2)