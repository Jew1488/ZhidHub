n = int(input())
s = str(input()).split()
meth = int(s[0])
maxim = int(s[n-1])
defenceoftheancientstwo = s[n//2 + 1]
for i in range(n):
    if(min(int(i), int(s[n - i - 1])) > defenceoftheancientstwo or max(int(i), int(s[n - i - 1])) > defenceoftheancientstwo):
        