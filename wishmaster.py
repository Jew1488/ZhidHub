def heap(a):
    if(len(a) <= 1):
        return a
    max = 0
    for i in range(1, len(a)):
       if(a[max] < a[i]):
           max = i
    a[-1],a[max] = a[max], a[-1]
    plus = a[-1]
    a.pop()
    return heap(a) + [plus]
a = str(input()).split()
for i in range(len(a)):
    a[i] = int(a[i])
print(heap(a))
