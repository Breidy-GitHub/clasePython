print("Usuario piense un numero \n"
        "Sumele 5 al numero \n"
        "Luego multipliquelo por 3 \n"
        "Por ultimo restele 15")
user=int(input("Por favor ingrese el resultado obtenido: \n"))
#Operacion
userdiv=user/3

print("El numero en el cual pensastes es: ",round(userdiv), "\n"
      "¿Es correcto este valor?\n")
value=input("Digite S si es correcto o N si no es incorrecto: \n")

if value=="S" or value=="s":
    print("Soy todo un adivino")
else: 
    print("Rectifica las cuentas te daras cuenta que no me equivoco")


