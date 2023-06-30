def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0] == '0' or s[0] == '1' or s[0] == '2' or s[0] == '3' or s[0] == '4' or s[0] == '5' or s[0] == '6' or s[0] == '7' or s[0] == '8' or s[0] == '9':
        return int(s[0])
    else:
        return -1