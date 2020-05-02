import math

i=1
while i>0:
    
    en=raw_input("ingrese la operacion(NOTA: para salir precione enter): ")+";"
    if en==";":
        break
    estado="q0"
    dato1=""
    dato2=""
    op=""
    for e in en:
        if estado=="q0":
            
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                estado="q2"
                dato1+=e
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0":
                estado="q1"
                dato1+=e
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==";":
                estado="qR"

        elif estado=="q1":
            
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0":
                estado="q1"
                dato1+=e
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="qR"
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==";":
                estado="qR"
            if e==" ":
                estado="q3"

        elif estado=="q2":
            
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="q2"
                 dato1+=e
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0" or e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==";":
                estado="qR"
            if e==" ":
                estado ="q3"
                
        elif estado=="q3":
            
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="q5"
                 op+=e
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#":
                estado="q4"
                op+=e
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0" or e==";":
                estado="qR"

        elif estado=="q5":
            
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="q5"
                 op+=e
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0" or e==";" or e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#":
                estado="qR"
            if e==" ":
                estado="q6"

        elif estado=="q4":
            
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0" or e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                estado="qR"
            if e==" ":
                estado="q8"

        elif estado=="q6":
            
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="q7"
                 dato2+=e
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0":
                estado="q9"
                dato2+=e
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==";" or e==" ":
                estado=="qR"

        elif estado=="q7":
            
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="q7"
                 dato2+=e
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0" or e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#":
                estado="qR"
            if e==";":
                estado="qA"

        elif estado=="q8":
           
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0":
                estado="q9"
                dato2+=e
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                estado="q7"
                dato2+=e
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==";" or e==" ":
                estado="qR"

        elif estado=="q9":
            
            if e=="1" or  e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="9" or e=="0":
                estado="q9"
                dato2+=e
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==" " or e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                estado="qR"
            if e==";":
                estado="qA"

    validacion = True

    if dato1=="uno":
        dato1 = 1
    elif dato1=="dos":
                     dato1 = 2
    elif dato1=="tres":
                     dato1 = 3
    elif dato1=="cuatro":
                     dato1 = 4
    elif dato1=="cinco":
                     dato1 = 5
    elif dato1=="seis":
                     dato1 = 6
    elif dato1=="siete":
                     dato1 = 7
    elif dato1=="ocho":
                     dato1 = 8
    elif dato1=="nueve":
                     dato1 = 9
    elif dato1=="diez":
                     dato1 = 10
    else:
        try:
            dato1 = float(dato1)
        except:
            print "su primer dato no es un numero"
            validacion = False
        
                     
    if op=="mas" or op=="suma":
                    op="+"
    elif op=="menos" or op=="resta":
                    op="-"
    elif op=="multiplicacion" or op=="por":
                    op="*"
    elif op=="divicion" or op=="entre":
                    op="/"
    elif op=="raiz":
                    op="#"
    elif op=="elevado":
                    op="^"
    elif op=="seno" or op=="sen" or op=="sin":
                    op="sen"
    elif op=="coseno" or op=="cos":
                    op="cos"
    elif op=="tangente" or op=="tan":
                    op="tan"
 
                
    if dato2=="uno":
                     dato2 = 1
    elif dato2=="dos":
                     dato2 = 2
    elif dato2=="tres":
                     dato2 = 3
    elif dato2=="cuatro":
                     dato2 = 4
    elif dato2=="cinco":
                     dato2 = 5
    elif dato2=="seis":
                     dato2 = 6
    elif dato2=="siete":
                     dato2 = 7
    elif dato2=="ocho":
                     dato2 = 8
    elif dato2=="nueve":
                     dato2 = 9
    elif dato2=="diez":
                     dato2 = 10
    else:
        try:
            dato2 = float(dato2)
        except:
            print "su segundo dato no es un numero"
            validacion = False

    if validacion:
        
        dato1=float(dato1)
        dato2=float(dato2)
        res=0

        if op=="+" or op=="-" or op=="*" or op=="/" or op=="#" or op=="^" or op=="sen" or op=="cos" or op=="tan":
            if op=="+":
                res=dato1 + dato2
            elif op=="-":
                res=dato1 - dato2
            elif op=="*":
                res=dato1 * dato2
            elif op=="/":
                res=dato1 / dato2
            elif op=="#":
                res=dato1 ** (1/dato2)
            elif op=="^":
                res=dato1**dato2
            elif op=="sen":
                res=math.sin(dato2)
            elif op=="cos":
                res=math.cos(dato2)
            elif op=="tan":
                res=math.tan(dato2)

            print ("el resultado de su operacion es: %s %s %s = %s"%(dato1,op,dato2,res))

        else:
            print ("operacion incorrecta")
