s = (str(input())).split()
maxim = int(s[0])
for y in s:
    if(s.count(y) > maxim):
        maxim = int(y)
print(maxim)
