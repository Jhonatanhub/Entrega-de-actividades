def Mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def McdCuatroNumeros(num1, num2, num3, num4):
    mcd_ab = Mcd(num1, num2)
    mcd_cd = Mcd(num3, num4)
    mcd_total = Mcd(mcd_ab, mcd_cd)
    print(f"El máximo común divisor de los 4 números es {mcd_total}")

num1 = int(input("Ingrese el primer número \n"))
num2 = int(input("Ingrese el segundo número \n"))
num3 = int(input("Ingrese el tercer número \n"))
num4 = int(input("Ingrese el cuarto número \n"))

McdCuatroNumeros(num1, num2, num3, num4)
