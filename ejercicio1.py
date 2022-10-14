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