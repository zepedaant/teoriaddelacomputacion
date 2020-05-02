nombre = raw_input ("¿como te llamas? ")
print "tu nombre es %s" %(nombre)
edad = raw_input ("¿cual es tu edad? ")
edad = int (edad)
if edad >= 18:
    print "eres mayor"
else:
    print "eres menor"

palabra = "hola"

for letra in palabra:
    print letra


frutas = ["manzana","pera","mango"]
for fruta in frutas:
    print fruta


rango = range (0,10)
print rango
for i in range (0,10):
    print i
