block = 0
n = 1

while block < 5:
    password = input()

    if password == "FLDSMDFR21":
        milimeters = int(input())
        hamburger = milimeters//3

        while n <= hamburger:
            print("* "*n)
            n += 1

        break

    else:
        block += 1

if block == 5:
    print("FLDSMDFR bloqueada!")