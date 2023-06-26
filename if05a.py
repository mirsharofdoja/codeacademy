def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    if n//1000%10>a:
        a=n//1000%10
    if n//100%10>a:
        a=n//100%10
    if n//10%10>a:
        a=n//10%10
    if n%10>a:
        a=n%10
    return a