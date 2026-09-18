s = (str(input())).split()
for i in range(len(s)) :print(s[len(s) - 1] if i == 0 else s[i - 1], end = ' ')