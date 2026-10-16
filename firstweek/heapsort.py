def graf(a, n, i):
    xam = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[xam] < a[l]:
        xam = l
    if r < n and a[xam] < a[r]:
        xam = r
    if xam != i:
        a[i],a[xam] = a[xam],a[i]
        graf(a, n, xam)
def heap(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        graf(a, n, i)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        graf(a, i, 0)
    return a
a = str(input()).split()
for i in range(len(a)):
    a[i] = int(a[i])
print("Our massive:", a)
print("Sorted massive is:", heap(a))
