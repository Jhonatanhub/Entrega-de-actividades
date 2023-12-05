def Salario(horas_trabajadas, pago_hora):
    if horas_trabajadas > 40:
        horas_extra = horas_trabajadas - 40
        pago_hora_extra = pago_hora * 1.5
        sueldo_horas_extra = horas_extra * pago_hora_extra
        pago_semanal =  (horas_trabajadas - horas_extra) * pago_hora + sueldo_horas_extra
        
        print("El pago semanal del trabajador es: " , pago_semanal)
        
    else:
        pago_semanal = horas_trabajadas * pago_hora
        
        print("El pago semanal del trabajadro es: " , pago_semanal)
        
horas_trabajadas = int(input("Ingrese las horas trabajadas en la semana \n"))
pago_hora = int(input("Ingrese el pago por hora \n"))
Salario(horas_trabajadas, pago_hora)