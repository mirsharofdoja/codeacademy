import string


def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a] in string.digits and int(s[a])%2==1:
            x+=int(s[a])
        a+=1
    return x