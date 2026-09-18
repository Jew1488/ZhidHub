f10 = open('input.txt', 'r')
f2 = f10.readlines()
f10.close()
ans = 1
s = str('')
for i in range(len(f2)):
    s += f2[i]
for i in range(len(s) - 1):
    if((s[i] == '.' or s[i] == '?' or s[i] == '!') and (s[i+1] == ' ' or s[i+1] == '\n')):
        ans += 1
print(ans)
