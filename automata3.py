p = raw_input("inserta el numero ") + "*"
estado= "q0"

for ent in p:
    if estado=="q0":
        if ent=="0":
            estado="q1"
        if ent=="1":
            estado="q1"
        if ent=="*":
            estado="qr"
    elif estado=="q1":
        if ent=="0":
            estado="q2"
        if ent=="1":
            estado="q1"
        if ent=="*":
            estado="qr"
    elif estado=="q2":
        if ent=="0":
            estado="q0"
        if ent=="1":
            estado="qa"
        if ent=="*":
            estado="qr"
    elif estado == "qr" or estado=="qa":
        break


print estado
