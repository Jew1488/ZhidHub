def Pr(N, ans,k):
        if(N%k == 0):
            ans.append(k)
            return Pr(N//k, ans, k)
        elif(N != 1):
            return Pr(N, ans, k+1)
        else:
            return ans

N = int(input())
mn = []
if(N == 1):
    print("Нет")
else:
    print(Pr(N,mn ,2))