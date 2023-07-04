def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(list1)):
        if list1[i]==0:
            list1[i]=False
        else:
            list1[i]=True
    return list1