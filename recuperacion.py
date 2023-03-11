cuenta=1000000
print('Tu saldo en la cuenta es: ', cuenta)

while cuenta >=1:
    op=input('¿Desea despositar dinero en su cuenta o desea retirar? o escriba Fin para finalizar : ')
    if op =='Fin'or op=='fin':
        break
    elif op=='retirar' or op=='Retirar':
        ret=int(input('Cuanto desea retirar: '))
        cuenta-=ret
        print('Su saldo total en su cuenta es: ', cuenta)
    elif op=='depositar' or op=='Depositar':
        dep=int(input('Cuanto desea depositar: '))
        cuenta +=dep
        print('Su saldo total en su cuenta es: ', cuenta)
    else:
         print('Opción inválida. Por favor seleccione "Depositar" o "Retirar"')
         continue
      
print('Gracias por utilizar nuestro sistema.')
