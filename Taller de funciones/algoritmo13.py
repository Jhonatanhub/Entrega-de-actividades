def ElementosPositivos(lista):
    n_positivos = 0
    for elemento in lista:
        if elemento > 0:
            n_positivos += 1
    print(f"El número de elementos positivos en la lista es: {n_positivos}")

lista = []
cant_elementos = int(input("Ingrese cuántos elementos vas a agregar a la lista \n"))
for i in range(1,cant_elementos + 1,1):
    elementos=int(input("Ingrese un elemento \n"))
    lista.append(elementos)
ElementosPositivos(lista)
