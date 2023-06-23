def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    b=len(str(n))-1
    x=0
    y=0
    while b>=0:
        c=n//(10**b)%10
        b-=1
        if c==0:
            x+=1
        else:
            y+=1
    return y>x
print(main(111000011))