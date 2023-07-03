arr=[1,2,3,4,5]
def p1(arr):
    b=0
    x=0
    while b<len(arr):
        x+=arr[b]
        b+=1
    return x
def p2(arr):
    b=0
    x=0
    while b<len(arr):
        x+=arr[b]
        b+=2
    return x
def p3(arr):
    b=1
    x=0
    while b<len(arr):
        x+=arr[b]
        b+=2
    return x
def p4(arr):
    b=0
    x=0
    while b<len(arr):
        if arr[b]%2==0:
            x+=arr[b]
        b+=1
    return x
def p5(arr):
    b=0
    x=0
    while b<len(arr):
        if arr[b]%2==1:
            x+=arr[b]
        b+=1
    return x
def p6(arr,k,n):
    a=arr[k:n]
    b=0
    x=0
    while b<len(a):
        x+=a[b]
        b+=1
    return x
def p7(arr,k,n):
    a=arr[k:n]
    b=0
    x=0
    while b<len(a):
        x+=a[b]
        b+=2
    return x
def p8(arr,k,n):
    a=arr[k:n]
    b=1
    x=0
    while b<len(a):
        x+=a[b]
        b+=2
    return x
def p9(n):
    a=[]
    b=1
    while b<=n:
        a.append(b)
        b+=1
    return a