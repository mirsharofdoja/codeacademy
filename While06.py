def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a] in 'aeiou':
            x+=1
        a+=1
    return x