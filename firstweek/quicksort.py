def quick(a):
    print("Sorting...")
    print("Sorting..")
    print("Sorting.")
    if len(a) <= 1:
        return a
    op = a[len(a) // 2]
    bot = [x for x in a if x < op]
    mid = [x for x in a if x == op]
    top = [x for x in a if x > op]
    return quick(bot) + mid + quick(top)
a = str(input()).split()
for i in range(len(a)):
    a[i] = int(a[i])
print("Sorted massive:", quick(a))