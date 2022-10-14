#EJERCICIO1
num1= int(input("Introduce el primer número: "))
num2= int(input("Introduce el segundo número: "))
num3= int(input("Introduce el tercer número: "))
while True:
  if num1==0:
    print("Prueba de nuevo, el primer número no puede ser igual a 0")
  elif num3>num2>num1:
    print("Los números estan en orden ascendente")
  else:
    print("Los número están en orden descendente")
  break


