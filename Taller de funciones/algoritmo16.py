def ValorMayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    print(f"El número mayor de la lista es {mayor}") 
    
lista = []
cant_numeros = int(input("Ingrese cuántos elementos vas a agregar a la lista \n"))
for x in range(1, cant_numeros + 1, 1):
    numero = int(input("Ingrese un número \n"))
    lista.append(numero)
ValorMayor(lista)