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

print("\n\n\n\n")


#EJERCICIO2
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


#EJERCICIO3
texto = input("Introduce tu texto: ")
contador_letra = 0
for letra in texto:
  if letra == "a":
    contador_letra = contador_letra + 1
  elif texto == ".":
    break
print(f"En el texto aparecen {contador_letra} letras a.")

print("\n")


#EJERCICIO4
deportes = ["Baloncesto", "Futbol", "Tenis", "Golf", "Natación"]
print(deportes)

print("\n")

print(deportes[0],";",len(deportes[0]))
print(deportes[1],";", len(deportes[1]))
print(deportes[2],";", len(deportes[2]))
print(deportes[3],";", len(deportes[3]))
print(deportes[4],";", len(deportes[4]))
print("\n")

print(f"El elemento con mas caracteres es: ", deportes[0])
deportes.sort(key=len)
print(deportes)

deportes.sort(key=len, reverse = True)
print(deportes)

print("\n")