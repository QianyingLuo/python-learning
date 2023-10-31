texto = input("Introduzca un texto: ")
isAllText = texto.isalpha()
isAllDigits = texto.isdigit()
isCharactersAndNumbers = texto.isalnum()
print(isAllText)
print(isAllDigits)
print(isCharactersAndNumbers)

texto2 = input("Introduzca un texto: ")
posicion = texto2.find("mundo") 
if posicion != -1:
    resultado = texto2[posicion:]
    print(resultado)

print("-" *20)
print("Partiendo de una frase con diferentes palabras separadas por espacios, crear una lista donde cada elemento sea cada palabra del texto. Mostrar dicha lista y mostrar el número de veces que se encuentra la palabra mundo en esa lista")
texto3 = "Hola mundo mundo adios"
print("Texto=", texto3)
lista = texto3.split() 
print(lista)
print("Número de veces que aparece la palabra mundo:", texto3.count("mundo"))
print("Haciendo mi nueva funcionalidad")