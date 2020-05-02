i=1
while i>0:
    en=raw_input("ingrese su operacion (nota: para salir de enter): ")+";"
    if en==";":
        break
    dato1=""
    dato2=""
    opera=""
    estado="q0"
    for e in en:
         if estado =="q0":
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                 estado="q0"
                 dato1 +=e
            if e==" ":
                estado="q1"
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e==";":
                print e + " la opereracion es incorrecta"
                estado="qR"

         elif estado=="q1":
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#":
                estado="q2"
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                estado="q3"
                opera +=e
            if e==";" or e==" ":
                print e + " su operacion es incorrecta"
                estado="qR"

         elif estado =="q2":
            if e==";" or e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0" or e=="9":
                estado="qR"
            if e==" ":
                estado="q4"

         elif estado=="q3":
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m":
                estado="q3"
                dato2 +=e
            if e==";" or e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0" or e=="9":
                estado="qR"
            if e==" ":
                estado="q4"

         elif estado=="q4":
            if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0" or e=="9":
                 estado="q4"
            if e=="+" or e=="*" or e=="/" or e=="^" or e=="-" or e=="#":
                estado="qR"
            if e==";":
                estado="qA"

                if dato1=="uno":
                    


    print estado
