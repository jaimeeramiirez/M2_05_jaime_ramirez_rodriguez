#EJERCICIO1.- Para este ejercicio, la parte más "compleja" es utliziar el "While True" y las excepciones para pedirle al usuario que introduzca el primer número distinto de 0. A partir de ahí sencillamente, utilzaremos un condicional con el tamaño de los número para ver si están en orden ascendente o no
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
