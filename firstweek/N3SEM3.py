def nod(a, b, d):

    if(a%d + b%d == 0):

        return d

    else:

        return nod(a,b,d-1)





def dv(a,b,d,y,x, Y):

    K = y + 1

    if(abs((d - (y)*b)) < a):

        if((d - (K)*b)%a == 0):

            Y.append(K)

            return dv(a,b,d,K,x,Y)

    else:

        if(x + y > x+1+1):

            return dv(a,b,d,1,x+1,Y)

        else:

            return Y





stroka = str(input()).split()
a = int(stroka[0])
b = int(stroka[1])

if(a == 1 and b != 1):

    print(1, 0, 1)

elif(b == 1):

    print(0, 1, 1)

elif(a%b == 0):

    print(0,a//b, b)

else:

    d = (nod(a,b, min(a,b)))

    Y = dv(a,b,d, 1, 1, [1])

    print((d - (max(Y))*b)//a ,max(Y),d)