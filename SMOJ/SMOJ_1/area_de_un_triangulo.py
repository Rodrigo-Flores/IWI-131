import math

a = float(input())
b = float(input())
c = float(input())

s = (a+b+c)/2
area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)

print(area)
