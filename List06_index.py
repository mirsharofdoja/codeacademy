def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(list1)):
        if list1[i]==1:
            list1[i]=True
    return list1