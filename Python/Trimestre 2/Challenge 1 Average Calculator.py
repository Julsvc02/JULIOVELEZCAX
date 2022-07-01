a=int(input("Cuanto sacaste en el primer trimestre en esta materia?"))
b=int(input("Cuanto sacaste en el segundo  trimestre en esta materia?"))
c=int(input("Cuanto sacaste en el tercer trimestre en esta materia?"))

x=(a+b+c)
p=(x/3)
print("Tu promedio general es: ",p)

if(p>6):
  print("Aprobaste")

if(p==10):
  print("Vaya que eres un genio")

if(p<6):
  print("esfuerzate mas para la siguiente, sigue intentando ")