def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b:
        if a<c:
            return a
        if a>c:
            return c
    if b<a:
        if b<c:
            return b
        if b>c:
            return c