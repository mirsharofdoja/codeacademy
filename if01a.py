def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c:
        return a
    if a>b and a<c:
        return c
    if b>c and b>a:
        return b
    if b>c and b<a:
        return a