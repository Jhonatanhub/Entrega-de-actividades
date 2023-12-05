def ConvertirFecha(dia, mes, ano):
    dia = str(dia)
    mes = str(mes)
    
    ano = str(ano)[-2:]
    
    fecha = f"{dia}/{mes}/{ano}"
    print("La fecha ingresada es: " , fecha)
    
dia = int(input("Ingrese el día \n"))
mes = int(input("Ingrese el mes \n"))
ano = int(input("Ingrese el año \n"))
ConvertirFecha(dia,mes,ano)