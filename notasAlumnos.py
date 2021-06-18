NomAlu = []
ApeAlu = []
NotAlu = []

while 1==1:
  n=int(input("ingrese el numero de alumnos a procesar"))
  if n>0:
    break
for i in range(n):    #carga de datos
  while 1==1:
    print("Ingresar datos para el alumno ",i+1)
    NomAlu.append(input("ingrese el nombre del alumno15 "))
    ApeAlu.append(input("ingrese el apellido del alumno "))
    NotAlu.append(float(input("ingrese la nota del alumno ")))
    deseaConti=input("desea continuar")
    if(deseaConti=='no'):
        break
    if NotAlu[i]>=0 and NomAlu[i]!="" and ApeAlu[i]!="":

      break

# calcular promedio
SumNotAlu=0
for i in range(n):
  SumNotAlu+=NotAlu[i]
  print("Alumno: ", NomAlu[i]," ", ApeAlu[i], " ", NotAlu[i])

print("El promedio de notas es ",SumNotAlu/n)

# Calcular la mediana
ListNotAlu=NotAlu
ListNotAlu.sort()
Mediana=float()
if n%2==0:          # numero de elementos par
  Mediana=(ListNotAlu[int(n/2)-1]+ListNotAlu[int(n/2)])/2
else:
  Mediana=(ListNotAlu[int(n/2)])

print("La mediana es ", Mediana)

# Encontrar Maximo y Minimo
MaxNot=0
MinNot=9999
for i in NotAlu:
  if i>MaxNot: MaxNot=i
  if i<MinNot: MinNot=i
print("El valor maximo es ", MaxNot)
print("El valor minimo es ", MinNot)

# Definir histograma de frecuencias
VecNotAlu=set(NotAlu)       # para saber notas del vector
ListNotAlu=list(VecNotAlu)
ListNotAlu.sort()
FreNotAlu=[]
for i in ListNotAlu:
  FreNotAlu.append(0)
for i in NotAlu:
   j = ListNotAlu.index(i)
   FreNotAlu[j]+=1
Moda=0
j=0
for k,l in enumerate(ListNotAlu):
    print("La nota ", l, "Frecuencia = ", FreNotAlu[k] )
    if FreNotAlu[k]>Moda:
      Moda=FreNotAlu[k]
      j=l
print("La moda es = ", j, " con frecuencia = ", Moda)