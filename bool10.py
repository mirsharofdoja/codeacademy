def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    for i in range(1,int(a**(1/2))+1):
        if i**2==a:
            return True
    return False