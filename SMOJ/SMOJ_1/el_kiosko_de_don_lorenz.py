A = 600
B = 300
C = 800

a = int(input())
b = int(input())
c = int(input())
PAGADO = int(input())

TOTAL = (A*a) + (B*b) + (C*c)
VUELTO = PAGADO - TOTAL

print(f"TOTAL = {TOTAL}")
print(f"PAGADO = {PAGADO}")
print(f"VUELTO = {VUELTO}")
