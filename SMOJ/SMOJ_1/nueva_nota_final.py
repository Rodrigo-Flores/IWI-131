c1 = float(input())
c2 = float(input())
c3 = float(input())
c4 = float(input())
c5 = float(input())


nf = round(((c2+c3+c4)/3)*(((c1+c5)/2)/100),1)
nt = round((c1+c2+c3+c4+c5)/5,1)


print(f"Nota Final Z: {nf}")
print(f"Nota Final tradicional: {nt}")
