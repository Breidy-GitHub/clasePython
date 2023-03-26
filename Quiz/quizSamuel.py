deuda= 130
print('Tienes una deuda',deuda)

while deuda>=1:
    op=input('¿Desea realizar el pago total o abonar la deuda?: ')
    if op=='Pago' or op=='pago':
        vp=int(input('Cuanto desea pagar: '))
        deuda=deuda-vp
        print('Su deuda es: ', deuda)
    elif op=='abonar' or op=='Abonar':
        vp=int(input('Cuanto desea pagar: '))
        deuda=deuda-vp
        print('Su deuda actual es:', deuda)
    else:
        print('Opción inválida. Por favor seleccione "Pago" o "Abonar"')
print('Gracias por pagar su deuda')

