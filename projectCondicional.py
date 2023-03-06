userOption = input("User dice =")
computerOption = input("computer dice =")

if  userOption == computerOption:
    print("empate")
elif userOption == "piedra":
    if computerOption == "tijera":
        print("piedra gana a tijera")
        print("user gano!")
    else:
        print("papel gana a piedra")
        print("computer gano!")
elif userOption =="papel":
    if computerOption == "piedra":
        print("papel gana a piedra")
        print("user gano!")
    else:
        print("tijera gana a papel")    
        print("computer gana a papel!")    
elif userOption == "tijera":
    if computerOption =="papel":
        print("tijera gana a papel")
        print("user gano!")
    else:
        print("piedra gana a tijera")
        print("computer gano!")
