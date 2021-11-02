myStr = "hallo welt"
myStr2 = "hallo,welt"
#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("Hallo", "Hola"))
print(myStr.count("l"))
print(myStr.startswith("Hal"))
print(myStr.endswith("elt"))
print(myStr.split())
print(myStr2.split(","))
print(myStr2.find(","))
#print(len(myStr))
print(myStr2.index("e"))
print(myStr2.isnumeric())
print(myStr2.isalpha())

#Impresion de string por indice
print(myStr[0])
print(myStr[2])
print(myStr[4])
print(myStr[-2])

#Impresion de variable por definicion
print("El mensaje es: " + myStr) # formato clasico

print(f"El mensaje es: {myStr}")

print("El mensaje es: {0}".format(myStr))

