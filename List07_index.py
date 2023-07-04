def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(list1)):
        if list1[i]==0:
            list1[i]=False
    return list1