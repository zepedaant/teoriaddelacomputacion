p = raw_input("ingresa tu correo: ")+";"

est="q0"

for e in p:
    if e=="q0":
        if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l"  or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0" or e=="9":
            est="q1"
            
        if e=="@" or e==";" or e==":" or e=="," :
            est="qr"
    elif est=="q1":
        if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0" or e=="9":
            est="q1"
        if e=="@":
            est="q2"
        if e==";" :
            est="qr"
    elif est=="q2":
        if e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0"  or e=="9":
            est="q2"
        if e==".":
            est="q3"
        if e==";":
            est="qr"
    elif est=="q3":
        if  e=="q" or e=="w" or e=="e" or e=="r" or e=="t" or e=="y" or e=="u" or e=="i" or e=="o" or e=="p" or e=="a" or e=="s" or e=="d" or e=="f" or e=="g" or e=="h" or e=="j" or e=="k" or e=="l" or e=="z" or e=="x" or e=="c" or e=="v" or e=="b" or e=="n" or e=="m" or e=="1" or e=="2" or e=="3" or e=="4" or e=="5" or e=="6" or e=="7" or e=="8" or e=="0"  or e=="9":
            est="q3"
        if e==";":
            est="qa"
    elif est == "qr" or est=="qa":
        break


print est
