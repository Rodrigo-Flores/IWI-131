personas = int(input())
dinero = int(input())

if personas <= 0:
    print("error")

elif dinero <= 0:
    print("error")

elif personas > 4:
    print("error")

if personas == 1:
    if dinero < 176625:
        print(True)
    else:
        print(False)

elif personas == 2:
    if dinero < 286928:
        print(True)
    else:
        print(False)

elif personas == 3:
    if dinero < 381098:
        print(True)
    else:
        print(False)

elif personas == 4:
    if dinero < 466116:
        print(True)
    else:
        print(False)




