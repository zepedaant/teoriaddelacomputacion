palabra = raw_input ("ingresa al operacion a realizar ")+ ","

est="q0"

for ent in palabra:
    if est=="q0":
        if ent=="1" or ent=="2" or ent=="3" or ent=="4" or ent=="5" or ent=="6" or ent=="7" or ent=="8" or ent=="9" or ent=="0":
            est="q1"
        if ent=="+" or ent=="-":
            est="q0"
        if ent=="*" or ent=="/":
            est="qr"
    elif est=="q1":
        if ent=="1" or ent=="2" or ent=="3" or ent=="4" or ent=="5" or ent=="6" or ent=="7" or ent=="8" or ent=="9" or ent=="0":
            est="q1"
        if ent=="+" or ent=="*" or ent=="/" or ent=="-":
            est="q2"
        if ent=="+" or ent==""
