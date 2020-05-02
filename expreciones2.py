import re
import math
i=1

while i>0:
    expresion= r'^([0-9]+|[\w]+)\s([\+\-\/\*]+|[\w]+)\s([0-9]+|[\w]+)$'
    expresionn= r'^([\w]+)\s([0-9]+)$'
    resultado= re.compile(expresion)
    resultado1= re.compile(expresionn)
    prueba = raw_input("ingrese su operacion(de enter para salir): ")
    busqueda= re.search(expresion, prueba)
    busquedaa= re.search(expresionn,prueba)
    if prueba=="":
        break
    

    if busqueda:
        print busqueda.group(1)
        print busqueda.group(2)
        print busqueda.group(3)

        validacion = True

        if busqueda.group(1)=="uno":
            n2=1
        elif busqueda.group(1)=="dos":
            n2=2
        elif busqueda.group(1)=="tres":
            n2=3
        elif busqueda.group(1)=="cuatro":
            n2=4
        elif busqueda.group(1)=="cinco":
            n2=5
        elif busqueda.group(1)=="seis":
            n2=6
        elif busqueda.group(1)=="siete":
            n2=7
        elif busqueda.group(1)=="ocho":
            n2=8
        elif busqueda.group(1)=="nueve":
            n2=9
        elif busqueda.group(1)=="diez":
            n2=10
        else:
            try:
                n2 = float(busqueda.group(1))
            except:
                print "primer dato no es un numero"
                validacion = False
                
        if busqueda.group(2)=="mas" or busqueda.group(2)=="suma":
                        op="+"
        elif busqueda.group(2)=="menos" or busqueda.group(2)=="resta":
                        op="-"
        elif busqueda.group(2)=="multiplicacion" or busqueda.group(2)=="por":
                        op="*"
        elif busqueda.group(2)=="divicion" or busqueda.group(2)=="entre":
                        op="/"
        elif busqueda.group(2)=="+" or busqueda.group(2)=="-" or busqueda.group(2)=="/" or busqueda.group(2)=="*":
            op = (busqueda.group(2))
        else:
            print "operacion incorrecta"
            validacion = False

        if busqueda.group(3)=="uno":
            n3=1
        elif busqueda.group(3)=="dos":
            n3=2
        elif busqueda.group(3)=="tres":
            n3=3
        elif busqueda.group(3)=="cuatro":
            n3=4
        elif busqueda.group(3)=="cinco":
            n3=5
        elif busqueda.group(3)=="seis":
            n3=6
        elif busqueda.group(3)=="siete":
            n3=7
        elif busqueda.group(3)=="ocho":
            n3=8
        elif busqueda.group(3)=="nueve":
            n3=9
        elif busqueda.group(3)=="diez":
            n3=10
        else:
            try:
                n3 = int(busqueda.group(3))
            except:
                print "su segundo dato no es un numero"
                validacion = False

        if validacion:

            n2 = int(n2)
            n3 = int(n3)
            

            if op=="+":
                    res=n2+n3
                    
            elif op=="/":
                    res=n2/n3
                    
            elif op=="-":
                    res=n2-n3
                  
            elif op=="*":
                    res=n2*n3
            
            print ("el resutado es: %s %s %s = %s"%(n2,op,n3,res))
            

    elif busquedaa:
        print busquedaa.group(1)
        print busquedaa.group(2)

        n2=int (busquedaa.group(2))
        ret=0

        if busquedaa.group(1)=="sin" or busquedaa.group(1)=="seno":
                ret=math.sin(n2)
                print ("el resutado es: %s %s = %s"%(busquedaa.group(1),n2,ret))
        elif busquedaa.group(1)=="tan" or busquedaa.group(1)=="tangente":
                ret=math.tan(n2)
                print ("el resutado es: %s %s = %s"%(busquedaa.group(1),n2,ret))
        elif busquedaa.group(1)=="cos" or busquedaa.group(1)=="coseno":
                ret=math.cos(n2)
                print ("el resutado es: %s %s = %s"%(busquedaa.group(1),n2,ret))
                
        else:
            print "su operacion es incorrecta"  
        
    else:
        print"qr"
        
