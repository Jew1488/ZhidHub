S = str(input()).split()
n = int(S[0])
s = str(S[1])
for i in range(n//2):
    print(s*(i+1))
for i in range(n//2 - 1 + n%2, -1, -1):
    print(s*(i+1))