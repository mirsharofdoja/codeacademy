def p1(n):
    b=1
    while b<=n:
        print(b)
        b+=1
def p2(n):
    while n>=0:
        print(n)
        n-=1
def p3(n,m):
    while m>=n:
        if n%2==0:
            print(n)
        n+=1
def p4(n,m):
    while m>=n:
        if n%2==1:
            print(n)
        n+=1
def p5(n,m,k):
    while m>=n:
        print(n)
        n+=k
def p6(n):
    a=1
    while n>=a:
        if n%a==0:
            print(a)
        a+=1
def p7(n):
    a=0
    result=''
    while n>=a:
        result+=f'{a}'
        a+=1
    result=','.join(result)
    return result
def p8(n):
    a=0
    while n>0:
        a+=1
        n//=10
    return a
def p9(n):
    x=0
    while n>0:
        a=n%10
        if a%2==0:
            x+=1
        n//=10
    return x
def p10(n):
    x=0
    while n>0:
        x+=n%10
        n//=10
    return x
def p11(n):
    n=int(n)
    x=0
    while n>0:
        x+=n%10
        n//=10
    return x
def p12(n):
    x=0
    while n>0:
        a=n%10
        if a%2==1:
            x+=a
        n//=10
    return x
def p13(n):
    a=str(n)
    x=n%10
    n=n//10
    while n>0:
        if n%10>x:
            x=n%10
        n//=10
    return x,a.index(f'{x}')
def p14(n):
    x=n%10
    n=n//10
    while n>0:
        if n%10>x:
            x=n%10
        n//=10
    return x
