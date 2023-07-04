def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max_element=data[0]
    a=0
    while a<len(data):
        if data[a]>max_element:
            max_element=data[a]
        a+=1
    return max_element
    