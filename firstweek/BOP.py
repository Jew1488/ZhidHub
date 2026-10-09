n = int(input())        # колво предметов
w = str(input()).split()        # массы
for i in range(n):       # из Стр в Инт
    w[i] = int(w[i])
p = str(input()).split()        # цены
for i in range(n):          # из Стр в Инт
    p[i] = int(p[i])
W = int(input())            # пороговая масса
P = [[0 for j in range(W+1)] for i in range(n+1)]           # массив рюкзаков с заполненными 0 для S = 0 и k = 0
ans = [['' for j in range(W+1)] for i in range(n+1)]
for k in range(1, n+1):         # учитываем предметы до k и формируем рюкзак
    for S in range(1,W+1):          # повышаем грузоподъемность
        if(w[k-1] <= S):
            P[k][S] = max(p[k-1] + P[k-1][S-w[k-1]],P[k-1][S])
            if(p[k-1] + P[k-1][S-w[k-1]]> P[k-1][S] and k not in ans):
                ans[k][S] = ' ' + ans[k-1][S - w[k-1]] +  ' ' + str(k-1)
            else:
                ans[k][S] = ans[k-1][S]
        else:
            P[k][S] = P[k-1][S]
            ans[k][S] = ans[k-1][S]
print(P[-1][-1])        # вывод данных
print(P)
print(ans[-1][-1])
