n = int(input())
sr = str(input())
ans = str("")
for i in range(int((len(sr))/n)):
    pop = str("")
    for j in range(i*n, (i+1)*n):
        pop += (sr[j])
    top = ""
    for k in range(len(pop) ):
        top += pop[(len(pop) - 1 - k)]
    ans += top
print(ans)