palabra = "1011*"
estado = "q0"

for entrada in palabra:
    if estado == "q0":    
      if entrada =="0":
          estado = "q1"
      elif entrada == "1":
          estado= "q2"
    if estado =="q1":
        if entrada=="0":
            estado="q1"
        if entrada =="1":
            estado="q2"
        if entrada =="*":
            estado="qr"
    if estado =="q2":
        if entrada=="0":
            estado="q1"
        if entrada =="q1":
            estado="q2"
        if entrada =="*":
            estado="qa"

print estado
