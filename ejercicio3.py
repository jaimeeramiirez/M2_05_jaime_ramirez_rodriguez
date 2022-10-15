#EJERCICIO3.- Para este código hemos utlilizado un bucle "for" que contará el número de letras "a" que hay en nuestro texto, para ello crearemos la variable "contador_letra" que irá sumando 1 por cada vez que introduzcamos la letra a en el texto.
texto = input("Introduce tu texto: ")
contador_letra = 0
for letra in texto:
  if letra == "a":
    contador_letra = contador_letra + 1
  elif texto == ".":
    break
print(f"En el texto aparecen {contador_letra} letras a.")

print("\n")