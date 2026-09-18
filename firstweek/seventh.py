s = (str(input())).split()
maxim = int(s[0])
for x in s:
    if(s.count(x) > maxim):
        maxim = int(x)
print(maxim)
