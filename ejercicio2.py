#EJERCICIO2.- Este ejercicio es similar al anterior con la diferencia de que introduciremos los número en una lista y para hacer cualquier cosa haremos referencia a la posición del número en la lista. 

lista=[]
print("Introduce tres número diferentes: ")
print("\n")
for x in range(3):
  lista.append(input("Introduce un número: "))

print("\n")

if ((lista[0])==0):
  print("El primer número no es válido")
elif lista[0]<lista[1]<lista[2]:  
  print("Los números están en orden ascendente")
else:
  print("No estan en orden ascendente")
  
print("\n")
print(lista)  
print("\n")
