n = int(input())
puta = []
for i in range(n-1):
    s = int(input())
    puta.append(s)
puta.sort()
c = bool(0)
for i in range(n-1):
    if(puta[i] != i+1):
        c = 1
        print(i+1)
        break
if(c == 0):
    print(n)