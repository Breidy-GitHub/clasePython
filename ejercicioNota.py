totalScore=0

for i in range(1,5):
    print("Ingrese la calificacion obtenidad en el taller",i)
    score=float(input())
    totalScore=+score
    scoreFinal=score/4
    
print("Su nota final es: ",totalScore)

if 0.0 <=totalScore <=2.9:
    print("Reprobaste la asi")
    
elif 3.0 <= totalScore <=4.0:
    print("Pasaste raspando asignatura")
    
elif totalScore >4.0:
    print("Aprobaste con buenos resultados")
