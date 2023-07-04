import string


def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a] in string.digits and int(s[a])%2==0:
            x+=1
        a+=1
    return x