import string


def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a] in string.digits:
            x+=int(s[a])
        a+=1
    return x