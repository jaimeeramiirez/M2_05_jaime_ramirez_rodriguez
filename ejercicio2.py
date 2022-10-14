#EJERCICIO2

lista=[]
print("Introduce tres número diferentes: ")
print("\n")
for x in range(3):
  lista.append(input("Introduce un número: "))
print(lista)
print("\n")

if lista[0]<lista[1]<lista[2]:  
  print("Los números están en orden ascendente")
elif (lista[0]==0):
  print("El primer número no es válido")
else:
  print("No estan en orden ascendente")

print("\n")
