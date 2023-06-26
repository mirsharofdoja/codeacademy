def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    return f'"{s[len(s)//2]}"' if len(s)%2==1 else f'"{s[len(s)//2-1]}{s[len(s)//2]}"'
