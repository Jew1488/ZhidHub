def Fib(N,x,n1,n2):
    if N > 3:
        n1 = n2
        n2 = x
        x  = n2 + n1
        return Fib(N-1, x, n1, n2)
    else:
        return x
N = int(input())
if (N == 1 or N == 2):
    print(1)
else:
    print(Fib(N,2,1,1))