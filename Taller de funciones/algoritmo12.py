def ValidacionFecha(dia, mes, ano):
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
        print(f"La fecha {dia}/{mes}/{ano} es inválida")
    else:
        print(f"La fecha {dia}/{mes}/{ano} es válida")
        
        
dia = int(input("Ingrese el día \n"))
mes = int(input("Ingrese el mes \n"))
ano = int(input("Ingrese el año \n"))
ValidacionFecha(dia, mes, ano)
