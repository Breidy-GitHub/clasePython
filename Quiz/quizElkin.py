print('Combo 1:valor 10000 \nCombo 2:valor 11000\nCombo 3:valor 10000')
orden=int(input('¿cuantas veces quiere ordenar? '))
valorOrden=0
while  orden>=1:
    preg=int(input('¿que combo desea ordenar? '))
    if preg==1:
        valorOrden=valorOrden+10000
        orden=(orden-1)
    elif preg==2:
        valorOrden=valorOrden+11000
        orden=(orden-1)
    elif preg==3:
        valorOrden=valorOrden+10000
        orden=(orden-1)
else:
    print ('el valor total de la orden',valorOrden)
    res =input('¿quiere ordenar otro Combo?')
    if res=='si' or res=='Si':
        orden =(orden +1)
        preg=int(input('¿que combo desea ordenar? '))
    if preg==1:
        valorOrden=valorOrden+10000
        orden=(orden-1)
    elif preg==2:
        valorOrden=valorOrden+11000
        orden=(orden-1)
    elif preg==3:
        valorOrden=valorOrden+10000
        orden=(orden-1)
    print ('el valor total de la orden',valorOrden)