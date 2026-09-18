s = (str(input())).split()
for i in range(len(s)): print(s[i] + ' ' if s.count(s[i]) == 1 else '',  end = '')
