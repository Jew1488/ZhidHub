s = (str(input())).split()
for i in range(0, len(s) - 1, 2):
    s[i], s[i+1] = s[i+1], s[i]
for i in range(len(s)) :print(s[i], end = ' ')
