p = raw_input("inserta el numero ") + "*"
est="q0"

for ent in p:
    if est=="q0":
        if ent=="0":
            est="q0"
        if ent=="1":
            est="q1"
        if ent=="*":
            est="qR"
    elif est=="q1":
        if ent=="0":
            est="q1"
        if ent=="1":
            est="q2"
        if ent=="*":
            est="qR"
    elif est=="q2":
        if ent=="0":
            est="q2"
        if ent=="1":
            est="q3"
        if ent=="*":
            est="qR"
    elif est=="q3":
        if ent=="0":
            est="q3"
        if ent=="1":
            est="q1"
        if ent=="*":
            est="qA"
    

print est
