def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    a=[]
    b=len(str(x))-1
    while b>=0:
        c=x//(10**b)%10
        b-=1
        a.append(c)

    return a==reversed(a)

print(main(121))
