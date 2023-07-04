import string


def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a] in string.digits and int(s[a])%2==1:
            x+=1
        a+=1
    return x