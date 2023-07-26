puntos = float(input("Ingrese los puntos que tiene (Validos: 0.2, 0.4, 0.6 |Invalidos: Todos los intermedios): "))
nivel_1 = 'Inaceptable'
nivel_2 = 'Aceptable'
nivel_3 = 'Meritorio'
remuneracion = 2400
if (puntos == 0.0):
    pago = (remuneracion * puntos)
    print(f'Su nivel es {nivel_1} y su remuneraciín sera de {pago}')
elif (puntos == 0.4):
    pago = (remuneracion * puntos)
    print(f'Su nivel es {nivel_2} y su remuneraciín sera de {pago}')
else:
    pago = (remuneracion * puntos)
    print(f'Su nivel es {nivel_3} y su remuneraciín sera de {pago}')