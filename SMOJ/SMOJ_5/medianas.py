'''
import statistics as stats

cant = int(input())

l = []
for i in range(cant):
    v = int(input())
    l.append(v)

l.sort

print(int((stats.median(l)*2)))
'''

cant = int(input())

l = []
for i in range(cant):
    v = int(input())
    l.append(v)

l.sort()

if len(l)%2 == 0:
    new = len(l)/2
    media = (l[new] + l[new-1]) / 2

else:
    new = len(l)//2
    media = l[new]

print(int(media*2))
