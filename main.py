#EJERCICIO1
print("\n")
while True:
    num1 = input("Introduzca el primer número, el cual, debe ser disinto de 0: ")
  
    try:
        num1 = int(num1)
    except:
        pass
    else:

        if num1!=0:

            break
num2= int(input("Introduzca el segundo número: "))
num3= int(input("Introduzca el tercer número: "))

print("\n")

if (num3>num2>num1):
  print("Los números estan en orden ascendente")
else:
  print("Los números no están en orden ascendente")

print("\n\n\n")

#EJERCICIO2

lista=[]
print("Introduce tres número diferentes: ")
print("\n")
for x in range(3):
  lista.append(input("Introduce un número: "))
print(lista)
print("\n")

while(lista[0]==0):
  print("El primer número introducido no puede ser 0")
if (lista[0]==0):
  print("El primer número no es válido")
elif lista[0]<lista[1]<lista[2]:  
  print("Los números están en orden ascendente")
else:
  print("No estan en orden ascendente")
  
print("\n")
